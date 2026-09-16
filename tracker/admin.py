from django.contrib import admin
from .models import StateRace, Candidate, SocialPost, CollectionJob


@admin.register(StateRace)
class StateRaceAdmin(admin.ModelAdmin):
    list_display = ('state', 'year', 'is_active', 'created_at')
    search_fields = ('name', 'state')
    list_filter = ('year', 'is_active')


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'party', 'state_race', 'twitter_handle', 'created_at')
    search_fields = ('name', 'alias_keywords', 'party')
    list_filter = ('party', 'state_race__state')


@admin.register(SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    list_display = ('platform', 'author_handle', 'candidate', 'sentiment_label', 'sentiment_score', 'sentiment_engine', 'published_at')
    list_filter = ('platform', 'sentiment_label', 'sentiment_engine', 'state_race')
    search_fields = ('content', 'author_handle', 'author_name', 'external_id')
    readonly_fields = ('collected_at',)
    ordering = ('-published_at',)


@admin.register(CollectionJob)
class CollectionJobAdmin(admin.ModelAdmin):
    list_display = ('id', 'platform', 'status', 'posts_collected', 'triggered_by', 'created_at', 'completed_at')
    list_filter = ('status', 'platform', 'triggered_by')
    readonly_fields = ('created_at', 'completed_at')
