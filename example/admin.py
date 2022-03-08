from django.contrib import admin
from django_qrcodes.admin import LinkedQRCodeInline
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [LinkedQRCodeInline]
