"""* (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную
        работу с числительными, начинающимися с заглавной буквы. Например:
"""



def num_translate_adv(num):
    translate_word = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                      'seven': 'семь', 'eigth': 'восемь', 'nine': 'девять', 'ten': 'десять' }
    if num[0].isupper():
        print(translate_word.get(num.lower()).capitalize())
    else:
        print(translate_word.get(num))

num_translate_adv(input('Введите на английском число от 1 до 10:'))