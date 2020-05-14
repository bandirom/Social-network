from .views import PostRUDView, PostAPIView
from django.urls import path

app_name = 'articles-api'

urlpatterns = [
    path('', PostAPIView.as_view(), name='api-create'),
    # path('create/', PostCreateView.as_view(), name='api-create'),
    path('<slug>', PostRUDView.as_view(), name='api-rud'),

]
