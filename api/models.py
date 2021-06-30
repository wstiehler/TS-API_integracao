from django.db import models


class Vendas(models.Model):
    product_id = models.IntegerField()
    marketplace = models.CharField(max_length=50, verbose_name='marketplace')

    def __str__(self) -> str:
        return f'{self.marketplace}'
