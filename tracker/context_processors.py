from .models import SocialPost

def global_tracker_context(request):
    """Provides global counts and indicators across all templates."""
    try:
        total_count = SocialPost.objects.count()
    except Exception:
        total_count = 0
    return {
        'global_dispatches_count': total_count
    }
