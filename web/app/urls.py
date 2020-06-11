from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views
from .profile.views import ProfileView, image_upload_ajax
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('account/profile/<user>/image/', image_upload_ajax, name='image_upload'),
    path('account/profile/<user>', ProfileView.as_view(), name='user-profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]
