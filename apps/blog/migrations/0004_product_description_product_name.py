# Generated by Django 5.1.2 on 2024-10-10 09:01

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(default=1, verbose_name='Краткое описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Название продукта'),
        ),
    ]
