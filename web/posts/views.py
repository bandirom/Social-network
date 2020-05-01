from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import ArticleModel


class ArticleListView(ListView):
    queryset = ArticleModel.objects.all()  # <p>/<modelname>_list.html
    template_name = 'posts/articles_list.html'


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        slug = self.kwargs.get("slug")
        return get_object_or_404(ArticleModel, slug=slug)
        # return get_object_or_404(ArticleModel, id=id_)

