from . import models
from rest_framework import serializers


class CurrencyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Currency
        fields = ('name_currency', 'uid_currency',)