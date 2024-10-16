from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from apps.blog.models import Product  # assuming you have a Product model


class StaticViewSitemap(Sitemap):
    """Sitemap for static pages."""
    def items(self):
        return ['about', 'contact', 'categories']

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    """Sitemap for dynamic product pages."""
    def items(self):
        return Product.objects.all()  # returns all products in the sitemap

    def location(self, item):
        return reverse('product', args=[item.id])  # reverse URL for product


class ProductDetailSitemap(Sitemap):
    """Sitemap for product detail pages."""
    def items(self):
        return Product.objects.all()  # returns all products for detailed view

    def location(self, item):
        return reverse('detail', args=[item.id])  # reverse URL for product detail
