from django.urls import path, include, re_path
from converter.views import CurrencyListView, CurrencyConverter

urlpatterns = [
    path('currency_list/', CurrencyListView.as_view({'get': 'list'}), name='currency_list'),
    path('rates/', CurrencyConverter.as_view({'get': 'list'}), name='currency_converter')
]