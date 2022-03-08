from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django_qrcodes.models import LinkedQRCode

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=100)

    qrcodes = GenericRelation(LinkedQRCode)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
