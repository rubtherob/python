"""
Написать функцию-генератор rand_nums, генерирующую N случайных целых
чисел в диапазоне 1 до 100 (включительно). Количество чисел N, которое выдаст генератор передается в функцию через параметр:
"""


import random


def rand_nums(N):
    i=0
    number=random.randint(1, 100)
    while i<N and i<100:
        yield number
        number = random.randint(1, 100)
        i+=1

numbers=rand_nums(7)

try:
    print(next(numbers))
    print(next(numbers))


except StopIteration:
    pass