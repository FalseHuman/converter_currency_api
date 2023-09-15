from django.conf import settings
from rest_framework import viewsets,  status
from rest_framework.response import Response
from converter.utils import converter_currency
from converter.models import Currency
from converter.serializer import CurrencyListSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter

class CurrencyListView(viewsets.ModelViewSet):
    '''
    Список валют
    '''
    queryset = Currency.objects.all()
    serializer_class = CurrencyListSerializer


class CurrencyConverter(viewsets.ViewSet):
    '''
    Коневертер валют
    '''
    @extend_schema(
        parameters=[
            OpenApiParameter(name='from', 
                            required=True, 
                            type=str
            ),
            OpenApiParameter(name='to', 
                            required=True, 
                            type=str
            ),
            OpenApiParameter(name='value', 
                            required=True, 
                            type=str
            ),
        ],
    )

    def list(self, request, *args, **kwargs):
        try:
            currency_from = request.query_params['from']
            currency_to = request.query_params['to']
            value = request.query_params['value']
            result = converter_currency(settings.RBC_API, currency_from, currency_to, value)
            return Response(result, status=status.HTTP_200_OK)
        except KeyError:
            return Response({
                'error': 'Отсутствуют параметры для осуществления конвертации. Пример запроса /api/v1/rates?from=USD&to=RUR&value=1'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
