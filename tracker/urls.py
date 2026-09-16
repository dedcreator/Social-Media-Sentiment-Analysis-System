from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('candidate/<int:candidate_id>/', views.candidate_detail_view, name='candidate_detail'),
    path('api/collect/', views.collect_posts_ajax, name='api_collect'),
    path('api/wordcloud/', views.wordcloud_ajax, name='api_wordcloud'),
    path('api/test-sentiment/', views.test_sentiment_ajax, name='api_test_sentiment'),
    path('export/csv/', views.export_posts_csv, name='export_csv'),
]
