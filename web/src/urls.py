from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf.urls.static import static
from app.sitemaps import ArticleSitemap, StaticViewSitemap, ProfileSitemap


sitemaps: dict = {
    'articles': ArticleSitemap,
    'profile': ProfileSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', include('app.urls')),
    path('p/', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    # path('admin/defender/', include('defender.urls')),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
