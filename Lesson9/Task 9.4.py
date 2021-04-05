'''
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw() (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три производных класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе переопределить метод draw(). Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры каждого класса и положить их в список. Проитерироваться по этому списку и вызвать метод draw()
 для каждого элемента.
'''
class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')

list_Stationery = []
list_Stationery.append(Pen())
list_Stationery.append(Pencil())
list_Stationery.append(Handle())

for a in list_Stationery:
    a.draw()

