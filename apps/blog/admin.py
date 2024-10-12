from django.contrib import admin
from django.contrib.auth.models import Group

from apps.blog.models import (
    Category,
    TopLevelCategory,
    SubCategory,
    Product,
    ProductImage, ProductDetail, Contacts
)
from apps.blog.utils import image_preview
from django.utils.translation import gettext_lazy as _


class TopLevelCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'id')
    search_fields = ('translations__name',)
    list_filter = ('created_at',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(parent__isnull=True)

    def name(self, obj):
        return obj.safe_translation_getter('name', any_language=True) or 'Безымянный'

    name.short_description = 'Название категория'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None or obj.parent is None:
            form.base_fields.pop('parent', None)  # Remove the 'parent' field for top-level categories
        return form


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at', 'id')
    search_fields = ('translations__name', 'parent__translations__name')
    list_filter = ('parent', 'created_at')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(parent__isnull=False, parent__parent__isnull=True)

    def name(self, obj):
        return obj.safe_translation_getter('name', any_language=True) or 'Безымянный'

    name.short_description = 'Название подкатегория'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parent':
            kwargs['queryset'] = Category.objects.filter(parent__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ProductDetailInline(admin.TabularInline):
    model = ProductDetail
    extra = 1
    fields = ['diameter', 'size', 'weight']


class ProductImagesInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image']
    readonly_fields = ['_image']

    def _image(self, obj):
        image = obj.image
        return image_preview(image, height=100, width=100)

    _image.short_description = ''


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'category']
    search_fields = ['name']
    inlines = [ProductDetailInline, ProductImagesInline]

    def name(self, obj):
        return obj.name or 'Безымянный'


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'company_name', 'phone', 'created_at']
    ordering = ['-id']


admin.site.register(TopLevelCategory, TopLevelCategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)


