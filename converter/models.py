from django.db import models

class Currency(models.Model):
    name_currency = models.CharField(
        max_length=255, 
        verbose_name="Название валюты",
    )
    uid_currency = models.CharField(
        max_length=255, 
        verbose_name="Название валюты", 
        unique=True
    )

    class Meta:
        verbose_name = 'Список валют'
        verbose_name_plural = 'Список валют'
        ordering = ('name_currency',)


    def __str__(self) -> str:
        return self.name_currency
