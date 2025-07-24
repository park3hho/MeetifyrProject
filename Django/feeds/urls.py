from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.Feeds.as_view(), name="feed-list"),  # 피드 목록 조회
    path("<int:feed_id>",  views.FeedDetail.as_view(), name="feed-detail"),  # 피드 상세 조회, 수정, 삭제
    
]