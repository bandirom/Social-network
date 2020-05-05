from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, RedirectView
from .models import ArticleModel, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class ArticleListView(ListView):
    queryset = ArticleModel.objects.all()  # <p>/<modelname>_list.html
    template_name = 'posts/articles_list.html'
    model = ArticleModel
    paginate_by = 5
    context_object_name = 'articles'
    ordering = ['-timestamp']


class ArticleDetailView(DetailView):
    template_name = 'posts/article_detail.html'
    context_object_name = 'article'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(ArticleModel, slug=slug)

    def get_context_data(self, **kwargs):
        article = self.get_object()
        last_comments = article.comment_set.order_by('-timestamp')[:10]
        data = super().get_context_data(**kwargs)
        data['last_comments'] = last_comments
        return data


class LeaveComment(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(ArticleModel, slug=slug)
        article.comment_set.create(author=self.request.POST['name'], comment_text=self.request.POST['text'])
        return article.get_absolute_url()


class ArticleLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(ArticleModel, slug=slug)
        url = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url


class ArticleLikeAPIToggle(APIView):
    authentication_classes = [authentication.SessionAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, slug=None, format=None):
        obj = get_object_or_404(ArticleModel, slug=slug)
        url = obj.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False
        like_count = obj.likes.count()
        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
                like_count = obj.likes.count()
            else:
                liked = True
                obj.likes.add(user)
                like_count = obj.likes.count()
            updated = True
        data = {
            'updated': updated,
            'liked': liked,
            'likecount': like_count,
        }
        return Response(data)
