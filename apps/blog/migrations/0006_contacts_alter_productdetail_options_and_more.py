# Generated by Django 5.1.2 on 2024-10-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_productdetail_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Полное имя')),
                ('phone', models.CharField(blank=True, max_length=250, null=True, verbose_name='Телефон')),
                ('company_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Название компании')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Обратной связи',
                'verbose_name_plural': 'Обратной связи',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='productdetail',
            options={'ordering': ['id'], 'verbose_name': 'Подробности продукта', 'verbose_name_plural': 'Подробности продукта'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ['id'], 'verbose_name': 'Изображение продукта', 'verbose_name_plural': 'Изображение продукта'},
        ),
    ]
