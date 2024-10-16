
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.shortcuts import render
from django.views.generic.base import TemplateView
from config.sitemaps import StaticViewSitemap, ProductSitemap, ProductDetailSitemap
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
    'product_detail': ProductDetailSitemap,
}



urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('', include('apps.blog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

