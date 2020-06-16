from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import ArticleListView, ArticleDetailView, ArticleLikeToggle, \
    LeaveComment, ArticleLikeAPIToggle, ArticleCreateView, ArticleDeleteView, SectionView
from likes.models import LikeDislike
from likes.views import VotesView
from .models import ArticleModel, Comment

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),

    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('api/', include('posts.api.urls')),
    path('<section>/', SectionView.as_view(), name='section'),
    path('<section>/<slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<section>/<slug>/like/', ArticleLikeToggle.as_view(), name='like-toggle'),
    path('<section>/<slug>/api/like/', ArticleLikeAPIToggle.as_view(), name='like-api-toggle'),
    path('<section>/<slug>/leave_comment/', LeaveComment.as_view(), name='leave_comment'),
    path('<section>/<slug>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]

# likes
urlpatterns += [
    path('<section>/<slug>/like/',
         login_required(VotesView.as_view(model=ArticleModel, vote_type=LikeDislike.LIKE)),
         name='article_like'),
    path('<section>/<slug>/dislike/',
         login_required(VotesView.as_view(model=ArticleModel, vote_type=LikeDislike.DISLIKE)),
         name='article_dislike'),
    path('<section>/<slug>/comment/like/',
         login_required(VotesView.as_view(model=Comment, vote_type=LikeDislike.LIKE)),
         name='comment_like'),
    path('<section>/<slug>/comment/dislike/',
         login_required(VotesView.as_view(model=Comment, vote_type=LikeDislike.DISLIKE)),
         name='comment_dislike'),
]
