from django.db import models
from django.utils.translation import gettext as _
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(_("Название категория"), max_length=250, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name="Родитель категории", related_name='subcategories')

    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")

    objects = models.Manager()

    def __str__(self):
        str_name = self.name
        parent = self.parent

        while parent:
            str_name = f'{parent.name} / ' + str_name
            parent = parent.parent

        return str_name


class TopLevelCategory(Category):
    class Meta:
        proxy = True
        verbose_name = "1. Основная категория"
        verbose_name_plural = "1. Основная категория"


class SubCategory(Category):
    class Meta:
        proxy = True
        verbose_name = "2. Подкатегория"
        verbose_name_plural = "2. Подкатегория"


class Product(models.Model):
    name = models.CharField(_("Название продукта"), max_length=250, null=True, blank=True)  # Removed the comma
    description = CKEditor5Field(config_name='extends', verbose_name="Краткое описание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True,
                                 verbose_name='Категория', related_name="categoryProduct")
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")

    objects = models.Manager()

    def __str__(self):
        return self.name or 'Безымянный'

    class Meta:
        ordering = ["id"]
        verbose_name = _("3. Продукт")
        verbose_name_plural = _("3. Продукты")


class ProductDetail(models.Model):
    diameter = models.FloatField(default=0, null=True, blank=True, verbose_name='Диаметры')
    size = models.CharField(_('Размер, DxT'), max_length=250, null=True, blank=True)
    weight = models.FloatField(default=0, null=True, blank=True, verbose_name="Масса, кг")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True,
                                verbose_name="Продукт", related_name="productDetail")  # Remove the comma
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")

    objects = models.Manager()

    def __str__(self):
        return f"{self.product.name}: {self.diameter} - {self.size}"

    class Meta:
        ordering = ["id"]
        verbose_name = _("Подробности продукта")
        verbose_name_plural = _("Подробности продукта")


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True,
                             verbose_name='Продукт', related_name='productImage')
    image = models.ImageField(upload_to='media/product', null=True, blank=True, verbose_name='Продукт картинки')

    objects = models.Manager()

    class Meta:
        ordering = ["id"]
        verbose_name = _("Изображение продукта")
        verbose_name_plural = _("Изображение продукта")


class Contacts(models.Model):
    full_name = models.CharField(_("Полное имя"), max_length=250, null=True, blank=True)
    phone = models.CharField(_("Телефон"), max_length=250, null=True, blank=True)
    company_name = models.CharField(_("Название компании"), max_length=250, null=True, blank=True)
    comment = models.TextField(null=True, blank=True, verbose_name="Комментарий")
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")

    objects = models.Manager()

    class Meta:
        ordering = ["id"]
        verbose_name = _("4. Обратной связи")
        verbose_name_plural = _("4. Обратной связи")
