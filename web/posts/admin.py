from django.contrib import admin
from django.forms.utils import flatatt
from django.urls import reverse
from django.utils.html import format_html
from .models import ArticleModel, Comment

# admin.site.register(ArticleModel)
admin.site.register(Comment)


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'author', 'timestamp', 'is_published']

    def author_link(self, obj):
        author = obj.author

        opts = author._meta
        route = '{}_{}_change'.format(opts.app_label, opts.model_name)
        author_edit_url = reverse(route, args=[author.pk])
        return format_html(
            '<a{}>{}</a>', flatatt({'href': author_edit_url}), author.first_name)
    # Set the column name in the change list
    author_link.short_description = "Author"
    # Set the field to use when ordering using this column
    author_link.admin_order_field = 'author__firstname'
