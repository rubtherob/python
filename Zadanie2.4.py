"""
    Дан список, содержащий искажённые данные с должностями и именами сотрудников:
    ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

    Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран фразы вида: 'Привет, Игорь!
    Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?
"""

Given_list=['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for element in Given_list:

    for word in element.split():
        if word == element.split()[ len(element.split())-1]:
            print('Привет, ' + word.capitalize() + '!')
