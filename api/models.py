from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(default=100, null=True)

    def __str__(self) -> str:
        return self.title

    @classmethod
    def get_products(cls):
        return cls.objects.all()