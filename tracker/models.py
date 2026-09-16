import json
from django.db import models
from django.utils import timezone


class StateRace(models.Model):
    """Represents a 2027 Gubernatorial Election race in a specific state."""
    name = models.CharField(max_length=150, help_text="e.g. Lagos State 2027 Gubernatorial Election")
    state = models.CharField(max_length=100)
    year = models.IntegerField(default=2027)
    description = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['state']

    def __str__(self):
        return f"{self.state} ({self.year})"


class Candidate(models.Model):
    """Political candidate contesting or running in the 2027 gubernatorial election."""
    name = models.CharField(max_length=150)
    party = models.CharField(max_length=100, help_text="e.g. APC, PDP, LP, NNPP, ADC")
    state_race = models.ForeignKey(StateRace, on_delete=models.CASCADE, related_name='candidates')
    alias_keywords = models.TextField(
        help_text="Comma-separated keywords or aliases for automatic entity recognition, e.g. 'GRV, Rhodes-Vivour, Gbadebo'",
        default=""
    )
    bio = models.TextField(blank=True, default="")
    avatar_color = models.CharField(max_length=20, default="#3B82F6", help_text="Hex color for charts & badges")
    twitter_handle = models.CharField(max_length=100, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.party} - {self.state_race.state})"

    def get_keywords_list(self):
        """Returns lowercase list of matching keywords including candidate's name."""
        keywords = [self.name.lower()]
        if self.alias_keywords:
            for kw in self.alias_keywords.split(','):
                kw_clean = kw.strip().lower()
                if kw_clean and kw_clean not in keywords:
                    keywords.append(kw_clean)
        return keywords

    def get_sentiment_stats(self):
        """Returns sentiment count and percentages for this candidate."""
        posts = self.posts.all()
        total = posts.count()
        if total == 0:
            return {
                'total': 0,
                'positive': 0,
                'negative': 0,
                'neutral': 0,
                'pos_pct': 0,
                'neg_pct': 0,
                'neu_pct': 0,
                'net_sentiment': 0.0,
                'avg_score': 0.0,
            }
        
        pos = posts.filter(sentiment_label='Positive').count()
        neg = posts.filter(sentiment_label='Negative').count()
        neu = posts.filter(sentiment_label='Neutral').count()
        
        avg_score = posts.aggregate(models.Avg('sentiment_score'))['sentiment_score__avg'] or 0.0
        net_sentiment = ((pos - neg) / total) * 100

        return {
            'total': total,
            'positive': pos,
            'negative': neg,
            'neutral': neu,
            'pos_pct': round((pos / total) * 100, 1),
            'neg_pct': round((neg / total) * 100, 1),
            'neu_pct': round((neu / total) * 100, 1),
            'net_sentiment': round(net_sentiment, 1),
            'avg_score': round(avg_score, 3),
        }


class SocialPlatform(models.TextChoices):
    X = 'X', 'X (formerly Twitter)'
    FACEBOOK = 'Facebook', 'Facebook'
    YOUTUBE = 'YouTube', 'YouTube Comments'
    NEWS = 'News Comments', 'News Comment Section'


class SentimentLabel(models.TextChoices):
    POSITIVE = 'Positive', 'Positive'
    NEGATIVE = 'Negative', 'Negative'
    NEUTRAL = 'Neutral', 'Neutral'


class SocialPost(models.Model):
    """Social media post, comment, or news reaction relating to 2027 gubernatorial election."""
    platform = models.CharField(max_length=50, choices=SocialPlatform.choices, db_index=True)
    external_id = models.CharField(max_length=200, help_text="Unique ID from source platform", db_index=True)
    author_name = models.CharField(max_length=150, blank=True, default="Anonymous")
    author_handle = models.CharField(max_length=100, blank=True, default="")
    content = models.TextField()
    url = models.URLField(max_length=500, blank=True, default="")
    
    # Relationships
    candidate = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    state_race = models.ForeignKey(StateRace, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')

    # Sentiment Classification
    sentiment_label = models.CharField(max_length=20, choices=SentimentLabel.choices, db_index=True)
    sentiment_score = models.FloatField(default=0.0, help_text="Compound polarity score: -1.0 (very negative) to +1.0 (very positive)")
    pos_score = models.FloatField(default=0.0)
    neu_score = models.FloatField(default=0.0)
    neg_score = models.FloatField(default=0.0)
    sentiment_engine = models.CharField(max_length=50, default="VADER", help_text="Model used: VADER or Transformers/BERT")

    # Engagement
    likes_count = models.IntegerField(default=0)
    shares_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)

    # Timestamps
    published_at = models.DateTimeField(db_index=True)
    collected_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']
        unique_together = ('platform', 'external_id')
        indexes = [
            models.Index(fields=['platform', 'sentiment_label']),
            models.Index(fields=['candidate', 'sentiment_label']),
            models.Index(fields=['published_at', 'sentiment_label']),
        ]

    def __str__(self):
        return f"[{self.platform}] {self.sentiment_label} ({self.sentiment_score:.2f}) - {self.content[:60]}..."


class CollectionJob(models.Model):
    """Tracks background and automated post collection jobs."""
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('RUNNING', 'Running'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    ]

    platform = models.CharField(max_length=50, default='ALL')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    posts_collected = models.IntegerField(default=0)
    triggered_by = models.CharField(max_length=50, default='MANUAL_DASHBOARD')
    log_message = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Job #{self.id} [{self.platform}] - {self.status} ({self.posts_collected} posts)"
