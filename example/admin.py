from django.contrib import admin
from django.utils.html import format_html
from django_qrcodes.admin import QRCodeAdminMixin

from .models import Product


@admin.register(Product)
class ProductAdmin(QRCodeAdminMixin):
    list_display = ['name']
