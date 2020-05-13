from django.db.models import Q
from rest_framework import generics, mixins
from ..models import ArticleModel
from .serializers import ArticleSerializer
from  .permissions import IsOwnerOrReadOnly


class PostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'slug'
    serializer_class = ArticleSerializer
    # permission_classes = []  # was setting in settings.py

    def get_queryset(self):
        qs = ArticleModel.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content_full__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRUDView(generics.RetrieveUpdateDestroyAPIView):  # DetailView, Create, FormView
    lookup_field = 'slug'
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return ArticleModel.objects.all()

    def get_object(self):
        slug = self.kwargs.get('slug')
        return ArticleModel.objects.get(slug=slug)


class PostListCreateView(generics.ListCreateAPIView):  # Create
    lookup_field = 'slug'
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return ArticleModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
