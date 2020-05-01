from django.contrib import admin

from .models import ArticleModel, Comment

admin.site.register(ArticleModel)
admin.site.register(Comment)