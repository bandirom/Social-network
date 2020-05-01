from django.urls import path
from .views import ArticleListView, ArticleDetailView
from .views import leave_comment

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<slug>/leave_comment/', leave_comment, name='leave_comment'),
]
