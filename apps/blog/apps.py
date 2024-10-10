from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _  # Import gettext_lazy


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.blog'
    verbose_name = _("Продукты и категории")  # Use lazy translation
