from django.db import models

class Category(models.Model):
    name = models.CharField("Название", max_length=256)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
