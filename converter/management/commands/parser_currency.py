from django.core.management.base import BaseCommand
from django.conf import settings
from converter.utils import get_currency_list
from converter.models import Currency


class Command(BaseCommand):
    help = 'Парсер валют'

    def handle(self, *args, **kwargs):
        list_currency = get_currency_list(settings.RBC_LIST_CURRENCY)
        for currency in list_currency:
            Currency.objects.get_or_create(
                name_currency=currency['name'], 
                uid_currency=currency['code']
            )
