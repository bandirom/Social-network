from django.conf import settings
from django.db import models
import datetime

from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone


class ArticleModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=120, null=False, blank=True)
    content_short = models.TextField('Short description', null=True, blank=True)
    content_full = models.TextField('Post text', null=True, blank=True)
    timestamp = models.DateTimeField('Published date', auto_now_add=True)
    slug = models.SlugField(verbose_name='Url', unique=True, blank=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.timestamp >= (timezone.now() - datetime.timedelta(days=7))

    def author_name(self):
        return str(self.author.username)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ArticleModel, self).save(*args, **kwargs)

    def slug_title(self):
        return slugify(self.title)

    def get_absolute_url(self):
        # return reverse("articles:article-detail", kwargs={"id": self.id})

        return reverse("articles:article-detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Comment(models.Model):
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    author = models.CharField('Author name', max_length=50)
    comment_text = models.CharField('Comment', max_length=200)
    timestamp = models.DateTimeField('Published  date', auto_now_add=True)  # auto_now_add=True,

    def comment_date(self):
        return self.timestamp

    def __str__(self):
        return self.author
