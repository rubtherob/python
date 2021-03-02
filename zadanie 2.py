user_number=int(input('Введите число в котором нужно посчитать сумму цифр: '))


def sum_number(number):
    summ=0
    while number > 10:
        summ=summ+(number%10)
        number=number//10
    summ = summ + (number % 10)
    return summ


while user_number!=0:
    print('Сумма цифр',sum_number(user_number))
    user_number=int(input('Введите число в котором нужно посчитать сумму цифр: '))



