from django.db import models
from ckeditor.fields import RichTextField


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
