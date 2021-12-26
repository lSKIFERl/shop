from django.db import models


class Category(models.Model):
    name = models.CharField("Name", max_length=256)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField('Name', max_length=256)
    price = models.DecimalField('Price', max_digits=6, decimal_places=2)
    description = models.TextField('Description')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImage(models.Model):
    image = models.ImageField('Picture', upload_to='imgs/')
    product = models.ForeignKey(Product, verbose_name='Product picture', on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name
