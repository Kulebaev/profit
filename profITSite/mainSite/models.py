from django.db import models

class Product(models.Model):
    ref_key = models.CharField(max_length=255, verbose_name='Внешний код', default="default_ref_key")
    name = models.CharField(max_length=255, verbose_name='Наименование')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name, self.price, self.ref_key

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
