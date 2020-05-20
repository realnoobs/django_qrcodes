from django.db import models
from django.contrib import admin
from django_qrcodes.models import QRCodeMixin

# Create your models here.

class Product(QRCodeMixin):
    class Meta:
        verbose_name = "Product"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name