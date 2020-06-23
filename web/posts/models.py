from django.conf import settings
from django.db import models
from datetime import datetime, timedelta
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.reverse import reverse as api_reverse
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import LikeDislike


def article_upload_path(instance, filename):
    """file will be uploaded to MEDIA_ROOT / post_images / user_<id> / <year> / <month> / <day>_<filename>"""
    now = datetime.now()
    return f'post_images/user_{instance.author.id}_{instance.author.username}/{now.year}' \
           f'/Month-{now.month}/{now.day}_{filename}'


class Section(models.Model):
    class Meta:
        db_table = "section"

    title = models.CharField(max_length=200)
    url = models.SlugField(verbose_name='Url', max_length=50, unique=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:section", kwargs={"section": self.url})

    def save(self, *args, **kwargs):
        self.url = slugify(self.title, allow_unicode=True).lower()
        super(Section, self).save(*args, **kwargs)


class ArticleModel(models.Model):
    """Model db for posts"""

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-timestamp']

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=120, null=False, blank=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    content_short = models.TextField('Short description', null=True, blank=True)
    content_full = models.TextField('Post text', null=True, blank=True)
    timestamp = models.DateTimeField('Published date', auto_now_add=True)
    slug = models.SlugField(verbose_name='Url', unique=True, blank=True)
    image = models.ImageField(verbose_name='Post image', upload_to=article_upload_path, blank=True,
                              default='post_images/no-image-available.jpg')
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    is_published = models.BooleanField(default=True)
    votes = GenericRelation(LikeDislike, related_query_name='articles')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.timestamp >= (timezone.now() - timedelta(days=7))

    def author_name(self):
        return str(self.author.username)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True).lower()
        super(ArticleModel, self).save(*args, **kwargs)

    def slug_title(self):
        return slugify(self.title, allow_unicode=True)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"slug": self.slug, "section": self.section})

    def get_like_url(self):
        return reverse('articles:like-toggle', kwargs={"slug": self.slug, "section": self.section})

    def get_api_like_url(self):
        return reverse('articles:like-api-toggle', kwargs={"slug": self.slug, "section": self.section})

    def get_api_url(self):
        return api_reverse('articles-api:api-rud', kwargs={'slug': self.slug, "section": self.section})

    def get_like(self):
        return reverse('articles:article_like', kwargs={'slug': self.slug, "section": self.section})

    def get_dislike(self):
        return reverse('articles:article_dislike', kwargs={'slug': self.slug, "section": self.section})

    @property
    def owner(self):
        return self.author.username


class Comment(models.Model):
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    author = models.CharField('Author name', max_length=50)
    comment_text = models.CharField('Comment', max_length=200)
    timestamp = models.DateTimeField('Published  date', auto_now_add=True)  # auto_now_add=True,
    # votes = GenericRelation(LikeDislike, related_query_name='comments')

    def comment_date(self):
        return self.timestamp

    def __str__(self):
        return self.author

    def get_leave_comment_url(self):
        return reverse("articles:leave_comment", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
