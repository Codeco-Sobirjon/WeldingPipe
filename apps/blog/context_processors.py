from apps.blog.models import Category


def categories_processor(request):
    categories = Category.objects.filter(parent__isnull=True).all().order_by('id')
    return {'categories': categories}
