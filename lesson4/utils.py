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
