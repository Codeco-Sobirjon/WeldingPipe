from django.shortcuts import redirect

from apps.blog.models import Category, Contacts
from apps.blog.send_email import send_html_email


def categories_processor(request):
    categories = Category.objects.filter(parent__isnull=True).all().order_by('id')
    return {'categories': categories}


def make_order_processor(request):
    return {}