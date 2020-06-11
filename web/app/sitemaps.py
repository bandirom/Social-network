from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from posts.models import ArticleModel
from .profile.models import Profile


class ArticleSitemap(Sitemap):

    def items(self):
        return ArticleModel.objects.all()


class ProfileSitemap(Sitemap):

    def items(self):
        return Profile.objects.all()


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['main:about']

    def location(self, obj):
        return reverse(obj)
