from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import ArticleModel, Comment


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


def leave_comment(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug)
    article.comment_set.create(author=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('articles:article-detail', args=(article.slug,)))

