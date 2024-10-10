from django.urls import path
from apps.blog.views import *




urlpatterns = [
    path('', indexView, name='index'),
    path('about/', aboutView, name="about"),
    path('contact/', contactView, name="contact"),
    path('categories/', categoriesView, name='categories'),
    path('product/<int:id>/', productsView, name='product'),
    path('detail/<int:id>/', product_detailView, name='detail')
]