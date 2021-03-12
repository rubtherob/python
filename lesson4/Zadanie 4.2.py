"""Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
Код валюты может быть в произвольном регистре.
Функция должна возвращать результат числового типа, например float.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
http://www.cbr.ru/scripts/XML_daily.asp.

Выведите на экран курсы для доллара и евро, используя написанную функцию.

Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере, посмотреть содержимое ответа.
"""

from requests import get



def get_currency_rate(valute):
    info_site=get('http://www.cbr.ru/scripts/XML_daily.asp').text
    info_site=info_site.replace('>',' ').replace('<',' ').split()
    counter=0
    valute=valute.upper()
    if valute in info_site:
        for element in info_site:
            if counter==2:
                print(valute,':',float(element.replace(',','.')))
                break
            if element==valute:
                counter=1
            if element=='Value' and counter==1:
                counter+=1
    else:
        return None

get_currency_rate('USD')