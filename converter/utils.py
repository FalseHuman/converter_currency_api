import requests
from bs4 import BeautifulSoup


def get_currency_list(url: str) -> list:
    '''
    Список валют с https://cash.rbc.ru/cash/currency.html
    '''
    page = requests.get(url=url)
    soup = BeautifulSoup(page.text, 'html.parser')
    list_currency = []
    for currency_text, currency_code in zip(soup.find_all('div', {'class': 'guide__cell js-currency-name'}),\
                                        soup.find_all('div', {'class': 'guide__cell js-currency-uid'})):
        list_currency.append(
            {'name': currency_text.text, 'code': currency_code.text})
    return list_currency


def converter_currency(url: str, currency_from: str, currency_to: str, value: str) -> dict:
    '''
    Конвертер валют с https://cash.rbc.ru/cash/currency.html
    '''
    response = requests.get(url=url, params={
        'currency_from': currency_from,
        'currency_to': currency_to,
        'source': 'cbrf',
        'sum': value
    })
    return response.json()