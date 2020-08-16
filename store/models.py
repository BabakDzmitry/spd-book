from django.db import models


class Book(models.Model):
    """Модель для книг"""
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
