from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from apps.blog.models import (
    Category,
    TopLevelCategory,
    SubCategory,
    Product,
    ProductImage, ProductDetail, Contacts
)


def indexView(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        company_name = request.POST.get('company_name')
        comment = request.POST.get('message')

        # Создаем объект Contacts и сохраняем его
        Contacts.objects.create(
            full_name=full_name,
            phone=phone,
            company_name=company_name,
            comment=comment
        )

        # После сохранения можно перенаправить пользователя на другую страницу, например, на ту же контактную страницу
        return redirect('index')  # Замените 'contact' на правильное имя URL


    return render(request, 'index.html')

def aboutView(request):

    return render(request, 'about.html')


def contactView(request):

    if request.method == "POST":
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        company_name = request.POST.get('company_name')
        comment = request.POST.get('message')

        # Создаем объект Contacts и сохраняем его
        Contacts.objects.create(
            full_name=full_name,
            phone=phone,
            company_name=company_name,
            comment=comment
        )

        # После сохранения можно перенаправить пользователя на другую страницу, например, на ту же контактную страницу
        return redirect('index')  # Замените 'contact' на правильное имя URL

    return render(request, 'contact.html')


def categoriesView(request):
    # Get main categories
    queryset = Category.objects.filter(parent__isnull=True).order_by('id')
    list_cate = []

    for main_cat in queryset:
        # Get subcategories for the current main category
        sub_category = Category.objects.filter(parent=main_cat).order_by('id')
        list_cate.append({
            'main_cat': main_cat,  # Save the individual main category
            'sub_cat': sub_category  # Save the corresponding subcategories
        })

    context = {
        'categories': queryset,
        'sub_categories': list_cate
    }

    return render(request, 'categories.html', context)


def productsView(request, id):
    queryset = get_object_or_404(Category, id=id)

    # Get all products for the given category
    product = Product.objects.select_related('category').filter(category=queryset).order_by('-id')

    # Set up pagination
    paginator = Paginator(product, 9)  # 9 products per page
    page_number = request.GET.get('page')  # Get the page number from the query parameters
    page_obj = paginator.get_page(page_number)  # Get the products for that page

    # Prepare the product list with images
    product_list = []
    for pro in page_obj:
        pro_images = ProductImage.objects.select_related('product').filter(product=pro).first()
        product_list.append({
            'pro': pro,
            'images': pro_images
        })

    context = {
        'product': product_list,
        'page_obj': page_obj,  # Pass the page object to the template
    }
    return render(request, 'product.html', context)


def product_detailView(request, id):
    queryset = get_object_or_404(Product, id=id)

    pro_images = ProductImage.objects.select_related('product').filter(product=queryset)
    pro_detail = ProductDetail.objects.select_related('product').filter(product=queryset)

    context = {
        'product': queryset,
        'images': pro_images,
        'detail': pro_detail
    }
    return render(request, 'detail.html', context)
