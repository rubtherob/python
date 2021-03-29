'''
 Написать скрипт, который выводит статистику для заданной папки в виде словаря,
  в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
  а значения — общее количество файлов (в том числе и в подпапках),
  размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
'''


import os

result_dict={}
def math_krat(arg):
    count=1
    while arg>=10:
        arg=arg//10
        count+=1
    return  10**count




list_post=[]
test = os.listdir('.')

for item in test:
    temp = os.path.splitext(item)
    if math_krat(os.stat(item).st_size) not in result_dict.keys():
        result_dict[math_krat(os.stat(item).st_size)]=1
    else:
        result_dict[math_krat(os.stat(item).st_size)] += 1
print(result_dict)