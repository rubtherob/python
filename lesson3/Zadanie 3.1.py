"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
"""

def num_translate(num):
    translate_word = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                      'seven': 'семь', 'eigth': 'восемь', 'nine': 'девять', 'ten': 'десять' }
    print(translate_word.get(num))

num_translate(input('Введите на английском число от 1 до 10:'))