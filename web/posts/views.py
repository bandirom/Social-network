from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, RedirectView, CreateView, DeleteView
from .models import ArticleModel, Section
from .forms import ArticleCreateForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .forms import CommentForm


class SectionView(View):
    template_name = 'posts/articles_list.html'

    def get(self, request, *args, **kwargs):
        data: dict = {}
        section = get_object_or_404(Section, url=self.kwargs['section'])
        data['section'] = section
        data['articles'] = ArticleModel.objects.filter(section=section).order_by('-timestamp')
        data['section_list'] = Section.objects.all().order_by('title')
        return render(request, template_name=self.template_name, context=data)


class ArticleMixin(object):
    model = ArticleModel
    context_object_name = 'article'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(self.model, slug=slug)


class ArticleListView(ArticleMixin, ListView):
    # queryset = ArticleModel.objects.all()  # <p>/<modelname>_list.html
    template_name = 'posts/articles_list.html'
    context_object_name = 'articles'
    paginate_by = 4
    ordering = ['-timestamp']

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['section_list'] = Section.objects.all().order_by('title')
        return data


class ArticleDeleteView(ArticleMixin, DeleteView):
    template_name = 'posts/article_delete.html'

    def get_success_url(self):
        return reverse("articles:article-list")


class ArticleDetailView(ArticleMixin, DetailView):
    template_name = 'posts/article_detail.html'

    def get_context_data(self, **kwargs):
        article = self.get_object()
        last_comments = article.comment_set.order_by('-timestamp')[:10]
        data = super().get_context_data(**kwargs)
        comment_form = CommentForm()
        data['comment_form'] = comment_form
        data['last_comments'] = last_comments
        return data


class ArticleCreateView(ArticleMixin, CreateView):

    template_name = 'posts/create_update.html'
    form_class = ArticleCreateForm

    # def get_context_data(self, **kwargs):
    #     print('get_context_data')
    #     super().get_context_data(**kwargs)
    #
    # def get(self, request, *args, **kwargs):
    #     print('get')
    #     super().get(request, *args, **kwargs)

    def post(self, request):
        form = ArticleCreateForm(request.POST)
        print('POST method', request.POST)

        if form.is_valid():
            article = form.save()
            article.save()
            return HttpResponseRedirect(reverse('articles:article-detail', args=[article.slug]))
        return render(request, 'posts/create-update.html', {'form': form})

    def form_valid(self, form):
        print('form_valid')
        print(form.cleaned_data)
        return super().form_valid(form)


class LeaveComment(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(ArticleModel, slug=slug)
        article.comment_set.create(author=self.request.POST['author'], comment_text=self.request.POST['comment_text'])
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

    def get(self, request, slug=None, section=None, format=None):
        obj = get_object_or_404(ArticleModel, slug=slug)
        # url = obj.get_absolute_url()
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
