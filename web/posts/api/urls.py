from .views import PostRUDView, PostListCreateView, PostAPIView
from django.urls import path


urlpatterns = [
    path('', PostAPIView.as_view(), name='api-create'),
    # path('create/', PostCreateView.as_view(), name='api-create'),
    path('<slug>', PostRUDView.as_view(), name='api-rud'),

]
