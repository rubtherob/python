"""
Создайте объект-генератор, выбирающий из функции-генератора rand_nums, написанного в предыдущем задании,только нечетные числа.
Проитерируйтесь по этому объекту-генератору и выведите на экран для каждого значения на отдельной строке:
 порядковый номер (начиная с 1-го) и соответствующее ему значение.
"""



import random


def rand_nums(N):
    i=0
    number=random.randint(1, 100)
    while i<N and i<100:
        yield number
        number = random.randint(1, 100)
        i+=1


rand_odd_nums=(num  for num in rand_nums(50) if num%2 == 1)


accumulator=0
for a,val in enumerate(rand_odd_nums,start=1):
    print(a,val)
    accumulator+=1
    if accumulator>99:
        break
