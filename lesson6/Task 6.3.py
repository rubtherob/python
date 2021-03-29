'''
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом —
 данные об их хобби. Известно, что при хранении данных используется принцип: одна строка —
 один пользователь, разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
 и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить
  сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
   Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много
    раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
4. * (вместо 3) Решить задачу 3 для ситуации, когда
объём данных в файлах превышает объём ОЗУ (разумеется, не нужно реально создавать такие большие файлы,
 это просто задел на будущее проекта). Также реализовать парсинг данных из файлов - получить отдельно фамилию,
 имя и отчество для пользователей и название каждого хобби:
  преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
  Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться данные,
  полученные в результате парсинга.
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
 чтобы можно было задать путь к обоим исходным файлам и путь к выходному файлу со словарём.
  Проверить работу скрипта для случая, когда все файлы находятся в разных папках.
'''


from tkinter import *
import tkinter.filedialog
from os import path
import pickle



def clicked1():
    global path1
    path1=tkinter.filedialog.askopenfilename(initialdir= path.dirname(__file__))

def clicked2():
    global path2
    path2=tkinter.filedialog.askopenfilename(initialdir= path.dirname(__file__))

def quit():
    global window
    window.destroy()

window = Tk()
window.title("Выбор пути для файла")
window.geometry('400x250')
lbl = Label(window, text="Выберите путь", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)
btn1 = Button(window, text="Путь для файла с ФИО!",command=clicked1)
btn1.grid(column=0, row=2)
btn2 = Button(window, text="Путь для файла с хобби!",command=clicked2)
btn2.grid(column=0, row=4)

btn3 = Button(window, text="Выбор",command=quit)
btn3.grid(column=0, row=10)
window.mainloop()



users_list=[]
hobby_list=[]
counter=0
result_dict={}

with open(path1,'r',encoding='utf-8') as users:
    for line in users:
        users_list.append(line.replace(',',' ').strip())

print(users_list)





with open(path2, 'r', encoding='utf-8') as hobby:
    for line in hobby:
        hobby_list.append(line.strip().split(','))

print(hobby_list)


while counter!=len(users_list):
    if counter<len(hobby_list):
       result_dict[users_list[counter]]=hobby_list[counter]
       counter+=1
    else:
        result_dict[users_list[counter]] = None
        counter += 1
print(result_dict)


with open('data.pickle', 'wb') as f:
    pickle.dump(result_dict, f)