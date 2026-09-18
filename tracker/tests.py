import json
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from tracker.models import StateRace, Candidate, SocialPost, SocialPlatform, CollectionJob
from tracker.sentiment_engine import analyze_post_sentiment
from tracker.collectors import SocialMediaCollector
from tracker.analytics import (
    generate_wordcloud_data,
    get_sentiment_trends,
    get_candidates_sentiment_summary,
    get_platform_sentiment_breakdown
)


class SentimentEngineTest(TestCase):
    def test_positive_sentiment(self):
        text = "This candidate has delivered phenomenal progress and outstanding economic reforms!"
        result = analyze_post_sentiment(text, engine='VADER')
        self.assertEqual(result['label'], 'Positive')
        self.assertGreater(result['score'], 0.05)

    def test_negative_sentiment(self):
        text = "A complete disaster of governance with terrible corruption, unpaved roads, and wasted funds."
        result = analyze_post_sentiment(text, engine='VADER')
        self.assertEqual(result['label'], 'Negative')
        self.assertLess(result['score'], -0.05)

    def test_neutral_sentiment(self):
        text = "The election commission announced polling unit guidelines for the 2027 race."
        result = analyze_post_sentiment(text, engine='VADER')
        self.assertEqual(result['label'], 'Neutral')


class ModelsAndAnalyticsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.race = StateRace.objects.create(
            name="Lagos 2027 Gubernatorial",
            state="Lagos",
            year=2027
        )
        self.candidate = Candidate.objects.create(
            name="Gbadebo Rhodes-Vivour",
            party="LP",
            state_race=self.race,
            alias_keywords="GRV, Rhodes-Vivour",
            avatar_color="#10B981"
        )
        self.candidate2 = Candidate.objects.create(
            name="Tokunbo Abiru",
            party="APC",
            state_race=self.race,
            alias_keywords="Abiru, Tokunbo",
            avatar_color="#3B82F6"
        )

        # Create sample posts
        SocialPost.objects.create(
            platform=SocialPlatform.X,
            external_id="post_1",
            author_name="User1",
            author_handle="@user1",
            content="Gbadebo Rhodes-Vivour has a brilliant plan for 2027 #Lagos",
            candidate=self.candidate,
            state_race=self.race,
            sentiment_label='Positive',
            sentiment_score=0.75,
            published_at=timezone.now()
        )
        SocialPost.objects.create(
            platform=SocialPlatform.FACEBOOK,
            external_id="post_2",
            author_name="User2",
            author_handle="@user2",
            content="Tokunbo Abiru failed on promises for 2027 #Lagos",
            candidate=self.candidate2,
            state_race=self.race,
            sentiment_label='Negative',
            sentiment_score=-0.65,
            published_at=timezone.now()
        )

    def test_candidate_keywords(self):
        keywords = self.candidate.get_keywords_list()
        self.assertIn("gbadebo rhodes-vivour", keywords)
        self.assertIn("grv", keywords)
        self.assertIn("rhodes-vivour", keywords)

    def test_candidate_sentiment_stats(self):
        stats = self.candidate.get_sentiment_stats()
        self.assertEqual(stats['total'], 1)
        self.assertEqual(stats['positive'], 1)
        self.assertEqual(stats['negative'], 0)
        self.assertEqual(stats['net_sentiment'], 100.0)

    def test_analytics_helpers(self):
        qs = SocialPost.objects.all()
        summary = get_candidates_sentiment_summary(qs)
        self.assertEqual(len(summary['candidates']), 2)
        self.assertIsNotNone(summary['most_positive'])
        self.assertEqual(summary['most_positive']['name'], "Gbadebo Rhodes-Vivour")

        trends = get_sentiment_trends(qs, days=7)
        self.assertTrue(len(trends['dates']) > 0)

        breakdown = get_platform_sentiment_breakdown(qs)
        self.assertIn(SocialPlatform.X, breakdown)
        self.assertEqual(breakdown[SocialPlatform.X]['total'], 1)

        wc_data = generate_wordcloud_data(qs, sentiment_filter='all')
        self.assertTrue(len(wc_data['word_frequencies']) > 0)


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.race = StateRace.objects.create(state="Kano", name="Kano 2027", year=2027)
        self.cand = Candidate.objects.create(name="Abba Yusuf", party="NNPP", state_race=self.race)
        self.post = SocialPost.objects.create(
            platform=SocialPlatform.X,
            external_id="ext_kano_1",
            author_name="KanoWatcher",
            author_handle="@kano",
            content="Abba Yusuf has done excellent work #KanoDecides2027",
            candidate=self.cand,
            state_race=self.race,
            sentiment_label='Positive',
            sentiment_score=0.8,
            published_at=timezone.now()
        )

    def test_dashboard_view(self):
        resp = self.client.get(reverse('tracker:dashboard'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "The Gubernatorial")
        self.assertContains(resp, "Abba Yusuf")

    def test_candidate_detail_view(self):
        resp = self.client.get(reverse('tracker:candidate_detail', args=[self.cand.id]))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Abba Yusuf")

    def test_collect_ajax_endpoint(self):
        from unittest.mock import patch
        with patch.object(SocialMediaCollector, 'collect_from_platform') as mock_collect:
            mock_post = SocialPost.objects.create(
                platform=SocialPlatform.X,
                external_id="mock_test_123",
                author_name="MockReporter",
                content="Mock election report",
                sentiment_label='Positive',
                published_at=timezone.now()
            )
            mock_collect.return_value = [mock_post]

            resp = self.client.post(
                reverse('tracker:api_collect'),
                data=json.dumps({'platform': 'X', 'count': 1, 'engine': 'VADER'}),
                content_type='application/json'
            )
            self.assertEqual(resp.status_code, 200)
            data = resp.json()
            self.assertTrue(data['success'])
            self.assertGreater(data['posts_collected'], 0)

    def test_wordcloud_ajax_endpoint(self):
        resp = self.client.get(reverse('tracker:api_wordcloud') + '?sentiment=Positive')
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertIn('word_frequencies', data)

    def test_sentiment_classify_ajax(self):
        resp = self.client.post(
            reverse('tracker:api_test_sentiment'),
            data=json.dumps({'text': 'Great progress in 2027!', 'engine': 'VADER'}),
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['result']['label'], 'Positive')

    def test_post_detail_view(self):
        resp = self.client.get(reverse('tracker:post_detail', args=[self.post.id]))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "DISPATCH RECORD")
        self.assertContains(resp, "KanoWatcher")

    def test_post_detail_json(self):
        resp = self.client.get(reverse('tracker:post_detail_json', args=[self.post.id]))
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data['id'], self.post.id)
        self.assertEqual(data['author_name'], "KanoWatcher")
        self.assertEqual(data['sentiment_label'], "Positive")

    def test_youtube_comment_permalink_and_working_url(self):
        yt_post = SocialPost.objects.create(
            platform=SocialPlatform.YOUTUBE,
            external_id="yt_comment_123",
            author_name="@citizen_commenter",
            author_handle="@citizen_commenter",
            content="Gbadebo Rhodes-Vivour has visionary plans for Lagos state in 2027.",
            url="https://www.youtube.com/watch?v=TEST_VID_123&lc=Ugy_TEST_COMMENT_ID",
            candidate=None,
            sentiment_label='Positive',
            sentiment_score=0.7,
            published_at=timezone.now()
        )
        self.assertIn("&lc=Ugy_TEST_COMMENT_ID", yt_post.working_url)
        self.assertEqual(yt_post.working_url, "https://www.youtube.com/watch?v=TEST_VID_123&lc=Ugy_TEST_COMMENT_ID")

        resp = self.client.get(reverse('tracker:post_detail', args=[yt_post.id]))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "View Comment on YouTube")

        json_resp = self.client.get(reverse('tracker:post_detail_json', args=[yt_post.id]))
        self.assertEqual(json_resp.status_code, 200)
        self.assertEqual(json_resp.json()['working_url'], "https://www.youtube.com/watch?v=TEST_VID_123&lc=Ugy_TEST_COMMENT_ID")

    def test_x_direct_tweet_working_url(self):
        x_post = SocialPost.objects.create(
            platform=SocialPlatform.X,
            external_id="x_1234567890",
            author_name="LagosPolls",
            author_handle="@lagospolls",
            content="Polls indicate high engagement ahead of 2027 race.",
            url="https://x.com/lagospolls/status/1234567890",
            candidate=None,
            sentiment_label='Neutral',
            sentiment_score=0.0,
            published_at=timezone.now()
        )
        self.assertEqual(x_post.working_url, "https://x.com/lagospolls/status/1234567890")

    def test_export_csv(self):
        resp = self.client.get(reverse('tracker:export_csv'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp['Content-Type'], 'text/csv')
        self.assertIn(b'Candidate', resp.content)

    def test_dispatches_view(self):
        resp = self.client.get(reverse('tracker:dispatches'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "All Recorded Dispatches")
        self.assertContains(resp, "KanoWatcher")

    def test_dispatches_search_and_filter(self):
        resp = self.client.get(reverse('tracker:dispatches') + '?q=Kano&sentiment=Positive')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "KanoWatcher")

    def test_test_analyzer_page_view(self):
        resp = self.client.get(reverse('tracker:test_analyzer'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Sentiment Polarity Inspector")
        self.assertContains(resp, "NLP Laboratory Workbench")

    def test_sentiment_classify_ajax_empty_text(self):
        resp = self.client.post(
            reverse('tracker:api_test_sentiment'),
            data=json.dumps({'text': '   ', 'engine': 'VADER'}),
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, 400)
        data = resp.json()
        self.assertFalse(data['success'])

    def test_sentiment_classify_ajax_entity_detection(self):
        resp = self.client.post(
            reverse('tracker:api_test_sentiment'),
            data=json.dumps({'text': 'Abba Yusuf is doing excellent work in Kano.', 'engine': 'VADER'}),
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['detected_entity']['candidate_name'], 'Abba Yusuf')
        self.assertEqual(data['detected_entity']['state_name'], 'Kano')



