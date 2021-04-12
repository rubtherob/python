'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
  год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
 месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''

class Date:
    date=''

    def __init__(self,date=''):
        Date.date=date

    @classmethod
    def time_date(cls):
        cls.day,cls.month,cls.year=cls.date.split('-')
        return (int(cls.day),int(cls.month),int(cls.year))

    @staticmethod
    def validate_date(day_month_year):
        if (day_month_year[0] <= 0) and (day_month_year[0] > 31):
            raise ValueError('Date incorrect')
        if day_month_year[1] not in range(1,13):
            raise ValueError('Date incorrect')




date1=Date('10-10-2021')
print(date1.time_date())
date1.validate_date(date1.time_date())


