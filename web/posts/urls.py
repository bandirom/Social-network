from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleLikeToggle, LeaveComment, ArticleLikeAPIToggle


app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<slug>/like/', ArticleLikeToggle.as_view(), name='like-toggle'),
    path('<slug>/api/like/', ArticleLikeAPIToggle.as_view(), name='like-api-toggle'),
    path('<slug>/leave_comment/', LeaveComment.as_view(), name='leave_comment'),

]
