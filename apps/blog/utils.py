from django.db.models import Q
from django.utils.html import format_html


def image_preview(image, width='', height=''):
    if image:
        image_url = image.url
        return format_html(f'<a href="{image_url}" target="_blank"><img src="{image_url}" width="{width}" ' 
                           f'height="{height}" style="object-fit: cover"></a>')
    return 'Нет изображения'
