import json
import csv
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.db.models import Count, Avg, Q
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from .models import SocialPost, Candidate, StateRace, SocialPlatform, SentimentLabel, CollectionJob
from .collectors import SocialMediaCollector
from .analytics import (
    generate_wordcloud_data,
    get_sentiment_trends,
    get_candidates_sentiment_summary,
    get_platform_sentiment_breakdown
)
from .sentiment_engine import analyze_post_sentiment


def dashboard_view(request):
    """Main interactive dashboard for 2027 Gubernatorial Election Sentiment Analysis."""
    # Filter parameters
    candidate_id = request.GET.get('candidate')
    platform_filter = request.GET.get('platform')
    sentiment_filter = request.GET.get('sentiment')
    state_id = request.GET.get('state')
    days_param = request.GET.get('days', '14')
    engine_filter = request.GET.get('engine')

    # Base queryset
    posts_qs = SocialPost.objects.select_related('candidate', 'state_race').all()

    # Apply date filter
    if days_param and days_param != 'all':
        try:
            days_int = int(days_param)
            start_date = timezone.now() - timedelta(days=days_int)
            posts_qs = posts_qs.filter(published_at__gte=start_date)
        except ValueError:
            days_int = 14
    else:
        days_int = 30

    # Apply additional filters
    if candidate_id and candidate_id.isdigit():
        posts_qs = posts_qs.filter(candidate_id=int(candidate_id))

    if platform_filter and platform_filter in [p[0] for p in SocialPlatform.choices]:
        posts_qs = posts_qs.filter(platform=platform_filter)

    if sentiment_filter and sentiment_filter in [s[0] for s in SentimentLabel.choices]:
        posts_qs = posts_qs.filter(sentiment_label=sentiment_filter)

    if state_id and state_id.isdigit():
        posts_qs = posts_qs.filter(state_race_id=int(state_id))

    if engine_filter:
        posts_qs = posts_qs.filter(sentiment_engine__icontains=engine_filter)

    total_posts = posts_qs.count()

    # Sentiment distribution
    pos_count = posts_qs.filter(sentiment_label=SentimentLabel.POSITIVE).count()
    neg_count = posts_qs.filter(sentiment_label=SentimentLabel.NEGATIVE).count()
    neu_count = posts_qs.filter(sentiment_label=SentimentLabel.NEUTRAL).count()

    pos_pct = round((pos_count / total_posts * 100), 1) if total_posts > 0 else 0
    neg_pct = round((neg_count / total_posts * 100), 1) if total_posts > 0 else 0
    neu_pct = round((neu_count / total_posts * 100), 1) if total_posts > 0 else 0

    avg_score = posts_qs.aggregate(Avg('sentiment_score'))['sentiment_score__avg'] or 0.0
    net_sentiment_score = round(pos_pct - neg_pct, 1)

    # Time-series trends
    trends_data = get_sentiment_trends(posts_qs, days=days_int)

    # Candidate sentiment ranking
    candidates_summary = get_candidates_sentiment_summary(posts_qs)

    # Platform breakdown
    platforms_data = get_platform_sentiment_breakdown(posts_qs)

    # Initial Word Cloud (overall)
    wordcloud_result = generate_wordcloud_data(posts_qs, sentiment_filter='all', max_words=70)

    # Recent posts preview
    recent_posts = posts_qs[:25]

    # Meta choices for filter dropdowns
    candidates_list = Candidate.objects.select_related('state_race').all()
    states_list = StateRace.objects.all()
    platforms_list = SocialPlatform.choices
    recent_jobs = CollectionJob.objects.all()[:5]

    context = {
        'total_posts': total_posts,
        'pos_count': pos_count,
        'neg_count': neg_count,
        'neu_count': neu_count,
        'pos_pct': pos_pct,
        'neg_pct': neg_pct,
        'neu_pct': neu_pct,
        'avg_score': round(avg_score, 3),
        'net_sentiment_score': net_sentiment_score,
        'trends_json': json.dumps(trends_data),
        'sentiment_dist_json': json.dumps({
            'labels': ['Positive', 'Neutral', 'Negative'],
            'counts': [pos_count, neu_count, neg_count],
            'colors': ['#10B981', '#64748B', '#EF4444']
        }),
        'candidates_summary': candidates_summary,
        'candidates_summary_json': json.dumps(candidates_summary['candidates']),
        'platforms_data': platforms_data,
        'platforms_data_json': json.dumps(platforms_data),
        'wordcloud_base64': wordcloud_result['image_base64'],
        'word_frequencies': wordcloud_result['word_frequencies'],
        'recent_posts': recent_posts,
        'candidates_list': candidates_list,
        'states_list': states_list,
        'platforms_list': platforms_list,
        'recent_jobs': recent_jobs,
        # Selected filter states
        'selected_candidate': candidate_id or '',
        'selected_platform': platform_filter or '',
        'selected_sentiment': sentiment_filter or '',
        'selected_state': state_id or '',
        'selected_days': days_param or '14',
    }

    return render(request, 'tracker/dashboard.html', context)


@csrf_exempt
@require_POST
def collect_posts_ajax(request):
    """Trigger real-time multi-source collection from the UI."""
    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception:
        data = request.POST

    platform = data.get('platform', 'ALL')
    count = int(data.get('count', 15))
    engine = data.get('engine', 'VADER')

    collector = SocialMediaCollector(engine=engine)
    if platform == 'ALL':
        job = collector.run_full_collection(count_per_platform=count, engine=engine, triggered_by='MANUAL_DASHBOARD')
        return JsonResponse({
            'success': True,
            'job_id': job.id,
            'posts_collected': job.posts_collected,
            'message': job.log_message
        })
    else:
        created = collector.collect_from_platform(platform=platform, count=count, engine=engine)
        return JsonResponse({
            'success': True,
            'posts_collected': len(created),
            'message': f"Collected {len(created)} election posts from {platform} using {engine}."
        })


@require_GET
def wordcloud_ajax(request):
    """Dynamic Word Cloud generator filtered by sentiment or candidate."""
    sentiment = request.GET.get('sentiment', 'all')
    candidate_id = request.GET.get('candidate')
    state_id = request.GET.get('state')

    posts_qs = SocialPost.objects.all()
    if candidate_id and candidate_id.isdigit():
        posts_qs = posts_qs.filter(candidate_id=int(candidate_id))
    if state_id and state_id.isdigit():
        posts_qs = posts_qs.filter(state_race_id=int(state_id))

    data = generate_wordcloud_data(posts_qs, sentiment_filter=sentiment, max_words=80)
    return JsonResponse(data)


@csrf_exempt
@require_POST
def test_sentiment_ajax(request):
    """Allows user to test custom post content live with VADER or Transformers."""
    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception:
        data = request.POST

    text = data.get('text', '').strip()
    engine = data.get('engine', 'VADER')

    if not text:
        return JsonResponse({'error': 'Please enter some text to analyze.'}, status=400)

    result = analyze_post_sentiment(text, engine=engine)
    return JsonResponse({
        'success': True,
        'result': result,
        'original_text': text
    })


def candidate_detail_view(request, candidate_id):
    """Deep-dive sentiment analytics page for a specific candidate."""
    candidate = get_object_or_404(Candidate.objects.select_related('state_race'), id=candidate_id)
    posts = candidate.posts.all()
    total_mentions = posts.count()

    stats = candidate.get_sentiment_stats()
    trends = get_sentiment_trends(posts, days=30)
    wordcloud_data = generate_wordcloud_data(posts, sentiment_filter='all', max_words=70)

    recent_posts = posts[:20]

    context = {
        'candidate': candidate,
        'stats': stats,
        'total_mentions': total_mentions,
        'trends_json': json.dumps(trends),
        'wordcloud_base64': wordcloud_data['image_base64'],
        'word_frequencies': wordcloud_data['word_frequencies'],
        'recent_posts': recent_posts,
    }
    return render(request, 'tracker/candidate_detail.html', context)


def export_posts_csv(request):
    """Exports filtered election posts to CSV format."""
    candidate_id = request.GET.get('candidate')
    platform_filter = request.GET.get('platform')
    sentiment_filter = request.GET.get('sentiment')

    posts_qs = SocialPost.objects.select_related('candidate', 'state_race').all()

    if candidate_id and candidate_id.isdigit():
        posts_qs = posts_qs.filter(candidate_id=int(candidate_id))
    if platform_filter:
        posts_qs = posts_qs.filter(platform=platform_filter)
    if sentiment_filter:
        posts_qs = posts_qs.filter(sentiment_label=sentiment_filter)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="election_2027_sentiment_posts.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'ID', 'Platform', 'Author', 'Candidate', 'State Race',
        'Sentiment Label', 'Sentiment Score', 'Pos Score', 'Neu Score', 'Neg Score',
        'Engine', 'Likes', 'Shares', 'Comments', 'Published At', 'Content', 'URL'
    ])

    for p in posts_qs[:2000]:
        writer.writerow([
            p.id,
            p.platform,
            p.author_handle or p.author_name,
            p.candidate.name if p.candidate else 'General',
            p.state_race.state if p.state_race else 'General',
            p.sentiment_label,
            p.sentiment_score,
            p.pos_score,
            p.neu_score,
            p.neg_score,
            p.sentiment_engine,
            p.likes_count,
            p.shares_count,
            p.comments_count,
            p.published_at.strftime('%Y-%m-%d %H:%M:%S'),
            p.content,
            p.url
        ])

    return response
