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
from apps.blog.send_email import send_html_email
from config import settings


def indexView(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        company_name = request.POST.get('company_name')
        comment = request.POST.get('message')
        email = request.POST.get('email')
        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')

        # Создаем объект Contacts и сохраняем его
        Contacts.objects.create(
            full_name=full_name,
            phone=phone,
            company_name=company_name,
            comment=comment,
            email=email,
            file1=file1,
            file2=file2
        )
        last_create = Contacts.objects.last()
        print(last_create.file1)
        print(last_create.file2)
        send_html_email(full_name, phone, company_name, comment, file1, file2, email)
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
        email = request.POST.get('email')
        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')

        # Создаем объект Contacts и сохраняем его
        Contacts.objects.create(
            full_name=full_name,
            phone=phone,
            company_name=company_name,
            comment=comment,
            email=email,
            file1=file1,
            file2=file2
        )
        last_create = Contacts.objects.last()

        send_html_email(full_name, phone, company_name, comment, last_create.file1, last_create.file2, email)

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
    # Get the category
    queryset = get_object_or_404(Category, id=id)

    # Get all products for the given category
    product = Product.objects.select_related('category').filter(category=queryset).order_by('-id')

    # Check if there are any products
    if not product.exists():
        # If no products, return the category description with a message
        context = {
            'product': [],
            'page_obj': None,  # No pagination needed
            'category': queryset
        }
        return render(request, 'product.html', context)

    # Get the first product
    product_first = product.first()

    # Get the category for the first product
    category = product_first.category if product_first else queryset

    # Set up pagination
    paginator = Paginator(product, 9)  # 9 products per page
    page_number = request.GET.get('page')  # Get the page number from the query parameters
    page_obj = paginator.get_page(page_number)  # Get the products for that page

    # Prepare the product list with images
    product_list = []
    for pro in page_obj:
        pro_images = ProductImage.objects.filter(product=pro).first()  # This retrieves the first image
        product_list.append({
            'pro': pro,
            'images': pro_images
        })

    context = {
        'product': product_list,
        'page_obj': page_obj,  # Pass the page object to the template
        'category': category
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
