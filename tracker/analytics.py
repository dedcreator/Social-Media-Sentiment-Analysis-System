import io
import re
import random
import base64
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count, Avg, Q
from django.db.models.functions import TruncDate
from wordcloud import WordCloud
from .models import SocialPost, Candidate, StateRace, SocialPlatform

# Stopwords for election discourse
COMMON_STOPWORDS = {
    'the', 'and', 'to', 'of', 'a', 'in', 'is', 'that', 'for', 'it', 'as', 'was', 'with', 'on', 'at',
    'by', 'this', 'be', 'are', 'from', 'or', 'an', 'they', 'which', 'one', 'you', 'were', 'her',
    'all', 'she', 'there', 'would', 'their', 'we', 'him', 'been', 'has', 'when', 'who', 'will',
    'more', 'no', 'if', 'out', 'so', 'said', 'what', 'its', 'about', 'into', 'than', 'them', 'can',
    'only', 'other', 'new', 'some', 'could', 'time', 'these', 'two', 'may', 'then', 'do', 'first',
    'any', 'my', 'now', 'such', 'like', 'our', 'over', 'man', 'me', 'even', 'most', 'made', 'after',
    'also', 'did', 'many', 'before', 'must', 'through', 'back', 'years', 'where', 'much', 'your',
    'way', 'well', 'down', 'should', 'because', 'each', 'just', 'those', 'people', 'mr', 'how', 'too',
    'little', 'state', 'candidate', 'election', '2027', 'gubernatorial', 'https', 'http', 'com', 'rt',
    'amp', 'vote', 'voting', 'governor', 'decides2027', 'decides', 'today', 'see', 'watch', 'one',
    'nbsp', 'href', 'font', 'span', 'html', 'target', 'blank', 'rel', 'strong', 'said', 'says', 'told'
}

def generate_wordcloud_data(posts_queryset, sentiment_filter: str = 'all', max_words: int = 80):
    """
    Generates both:
    1. Base64 encoded PNG image via wordcloud library
    2. JSON word frequency list for interactive UI
    """
    if sentiment_filter in ('Positive', 'Negative', 'Neutral'):
        posts = posts_queryset.filter(sentiment_label=sentiment_filter)
    else:
        posts = posts_queryset

    # Aggregate text
    texts = list(posts.values_list('content', flat=True))
    combined_text = " ".join(texts)

    if not combined_text.strip():
        return {
            'image_base64': None,
            'word_frequencies': [],
            'count': 0
        }

    # Clean text and calculate word frequencies
    words = re.findall(r'\b[a-zA-Z]{3,}\b', combined_text.lower())
    freqs = {}
    for w in words:
        if w not in COMMON_STOPWORDS:
            freqs[w] = freqs.get(w, 0) + 1

    sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)[:max_words]
    word_freq_dict = dict(sorted_freqs)
    word_freq_list = [{'text': k, 'weight': v} for k, v in sorted_freqs]

    image_base64 = None
    if word_freq_dict:
        try:
            # Paper / Editorial ink palettes
            def paper_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
                if sentiment_filter == 'Positive':
                    colors = ["#1b4332", "#2d6a4f", "#40916c", "#52b788", "#1e5e3a", "#14532d"]
                elif sentiment_filter == 'Negative':
                    colors = ["#7f1d1d", "#991b1b", "#b91c1c", "#dc2626", "#881337", "#9f1239"]
                else:
                    colors = ["#1c1917", "#292524", "#44403c", "#57534e", "#1e3a8a", "#0f172a"]
                import random
                return random.choice(colors)

            wc = WordCloud(
                width=800,
                height=400,
                background_color='#FAF9F6',  # tactile warm paper
                color_func=paper_color_func,
                stopwords=COMMON_STOPWORDS,
                max_words=max_words,
                contour_width=0,
                prefer_horizontal=0.9
            ).generate_from_frequencies(word_freq_dict)

            img_buffer = io.BytesIO()
            wc.to_image().save(img_buffer, format='PNG')
            image_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
        except Exception as e:
            logger_error = str(e)

    return {
        'image_base64': image_base64,
        'word_frequencies': word_freq_list,
        'count': len(texts)
    }


def get_sentiment_trends(posts_queryset, days: int = 14):
    """Computes daily aggregated sentiment counts and average sentiment score."""
    start_date = timezone.now() - timedelta(days=days)
    daily_stats = (
        posts_queryset.filter(published_at__gte=start_date)
        .annotate(date=TruncDate('published_at'))
        .values('date')
        .annotate(
            total=Count('id'),
            positive=Count('id', filter=Q(sentiment_label='Positive')),
            negative=Count('id', filter=Q(sentiment_label='Negative')),
            neutral=Count('id', filter=Q(sentiment_label='Neutral')),
            avg_score=Avg('sentiment_score')
        )
        .order_by('date')
    )

    dates = []
    positives = []
    negatives = []
    neutrals = []
    avg_scores = []

    for entry in daily_stats:
        if entry['date']:
            dates.append(entry['date'].strftime('%b %d'))
            positives.append(entry['positive'])
            negatives.append(entry['negative'])
            neutrals.append(entry['neutral'])
            avg_scores.append(round(entry['avg_score'] or 0.0, 3))

    return {
        'dates': dates,
        'positive': positives,
        'negative': negatives,
        'neutral': neutrals,
        'avg_scores': avg_scores
    }


def get_candidates_sentiment_summary(posts_queryset):
    """
    Computes sentiment distribution, net sentiment, and ranks candidates
    by most positive and most negative reactions.
    """
    candidates = Candidate.objects.select_related('state_race').all()
    candidate_data = []

    for cand in candidates:
        cand_posts = posts_queryset.filter(candidate=cand)
        total = cand_posts.count()
        if total == 0:
            continue

        pos = cand_posts.filter(sentiment_label='Positive').count()
        neg = cand_posts.filter(sentiment_label='Negative').count()
        neu = cand_posts.filter(sentiment_label='Neutral').count()
        avg_score = cand_posts.aggregate(Avg('sentiment_score'))['sentiment_score__avg'] or 0.0

        pos_pct = round((pos / total) * 100, 1)
        neg_pct = round((neg / total) * 100, 1)
        neu_pct = round((neu / total) * 100, 1)
        net_sentiment = round(((pos - neg) / total) * 100, 1)

        candidate_data.append({
            'id': cand.id,
            'name': cand.name,
            'party': cand.party,
            'state': cand.state_race.state,
            'color': cand.avatar_color,
            'total': total,
            'positive': pos,
            'negative': neg,
            'neutral': neu,
            'pos_pct': pos_pct,
            'neg_pct': neg_pct,
            'neu_pct': neu_pct,
            'net_sentiment': net_sentiment,
            'avg_score': round(avg_score, 3)
        })

    # Sort candidates
    by_positive = sorted(candidate_data, key=lambda x: (x['pos_pct'], x['total']), reverse=True)
    by_negative = sorted(candidate_data, key=lambda x: (x['neg_pct'], x['total']), reverse=True)
    by_mentions = sorted(candidate_data, key=lambda x: x['total'], reverse=True)

    most_positive_candidate = by_positive[0] if by_positive else None
    most_negative_candidate = by_negative[0] if by_negative else None
    most_discussed_candidate = by_mentions[0] if by_mentions else None

    return {
        'candidates': by_mentions,
        'most_positive': most_positive_candidate,
        'most_negative': most_negative_candidate,
        'most_discussed': most_discussed_candidate
    }


def get_platform_sentiment_breakdown(posts_queryset):
    """Breakdown of sentiment across platforms (X, Facebook, YouTube, News)."""
    platforms_data = {}
    for choice, label in SocialPlatform.choices:
        plat_posts = posts_queryset.filter(platform=choice)
        total = plat_posts.count()
        if total > 0:
            pos = plat_posts.filter(sentiment_label='Positive').count()
            neg = plat_posts.filter(sentiment_label='Negative').count()
            neu = plat_posts.filter(sentiment_label='Neutral').count()
            avg_score = plat_posts.aggregate(Avg('sentiment_score'))['sentiment_score__avg'] or 0.0
            platforms_data[choice] = {
                'label': label,
                'total': total,
                'positive': pos,
                'negative': neg,
                'neutral': neu,
                'pos_pct': round((pos / total) * 100, 1),
                'neg_pct': round((neg / total) * 100, 1),
                'neu_pct': round((neu / total) * 100, 1),
                'avg_score': round(avg_score, 3)
            }
        else:
            platforms_data[choice] = {
                'label': label,
                'total': 0,
                'positive': 0,
                'negative': 0,
                'neutral': 0,
                'pos_pct': 0,
                'neg_pct': 0,
                'neu_pct': 0,
                'avg_score': 0.0
            }
    return platforms_data
