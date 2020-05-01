from django.urls import path
from .views import ArticleListView, ArticleDetailView

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    # path('<id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<slug>/', ArticleDetailView.as_view(), name='article-detail'),
]
