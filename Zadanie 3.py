#Заполняем список
cube=[]
for j in range(1000):
    if j%2==1:
        cube.append(j**3)


# функция вычисляющая сумму цифр
def sum_number(number):
    summ=0
    while number > 10:
        summ=summ+(number%10)
        number=number//10
    summ = summ + (number % 10)
    return summ


#1 подпункт
amount_nuber=0
for i in cube:
    if sum_number(i)%7==0:
        amount_nuber=amount_nuber+i
print('Вывод для 3.1: ',amount_nuber)

#2 подпункт
amount_nuber=0
for i in cube:
    if (sum_number(i+17))%7==0:
        amount_nuber=amount_nuber+(i+17)
print('Вывод для 3.2: ',amount_nuber)

#3 подпункт
amount_nuber=0
for l in range(1000):
    if l%2==1:
        if (sum_number(l**3 + 17)) % 7 == 0:
            amount_nuber = amount_nuber + (l**3 + 17)
print('Вывод для 3.3: ',amount_nuber)