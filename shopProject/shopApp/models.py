from django.db import models
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=100)
    discript = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    registrant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
