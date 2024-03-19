from django.db import models
from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    margin = models.DecimalField(max_digits=10, decimal_places=2)
    package_code = models.CharField(max_length=255)

    def __str__(self):
        return self.title
