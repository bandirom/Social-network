from rest_framework import serializers
from ..models import ArticleModel


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = [
            'pk',
            'author',
            'title',
            'content_full',
            'timestamp',
            'is_published',
            'likes',
            'image',
        ]
        read_only_field = ['pk', 'author']

    def validate_title(self, attrs):  # title validation
        qs = ArticleModel.objects.filter(title__iexact=attrs)
        if self.instance:
            qs = qs.exclude(slug=self.instance.slug)
        if qs.exists():
            raise serializers.ValidationError('This title has already been used')
        return attrs
