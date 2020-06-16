from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views
from .models import LikeDislike
from posts.models import ArticleModel, Comment

# app_name = 'likes'
#
# urlpatterns = [
#     path('like/',
#          login_required(views.VotesView.as_view(model=ArticleModel, vote_type=LikeDislike.LIKE)),
#          name='article_like'),
#     path('dislike/',
#          login_required(views.VotesView.as_view(model=ArticleModel, vote_type=LikeDislike.DISLIKE)),
#          name='article_dislike'),
#     path('comment/like/',
#          login_required(views.VotesView.as_view(model=Comment, vote_type=LikeDislike.LIKE)),
#          name='comment_like'),
#     path('comment/dislike/',
#          login_required(views.VotesView.as_view(model=Comment, vote_type=LikeDislike.DISLIKE)),
#          name='comment_dislike'),
# ]
