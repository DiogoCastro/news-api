from django.urls import path
from news.api.views import (ArticleDetailAPIView,
                            ArticleListCreateAPIView,
                            JournalistDetailAPIView,
                            JournalistListCreateAPIView)

urlpatterns = [
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),
    path('journalists/', JournalistListCreateAPIView.as_view(), name='journalist-list'),
    path('journalists/<int:pk>/', JournalistDetailAPIView.as_view(), name='journalist-detail'),
]
