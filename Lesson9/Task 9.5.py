'''
Реализуйте базовый класс Car.
при создании класса должны быть переданы атрибуты: color (str), name (str).
реализовать в классе методы: go(speed), stop(), turn(direction), которые должны изменять состояние машины - для хранения этих
свойств вам понадобятся дополнительные атрибуты - придумайте какие.
добавьте метод is_police() - который возвращает True/False, в зависимости от того является ли этот автомобиль полицейским
 (см.дальше)
Сделайте несколько производных классов: TownCar, SportCar, WorkCar, PoliceCar;
Добавьте в базовый класс метод get_status(), который должен возвращать в виде строки название, цвет,
 текущую скорость автомобиля и направление движения (в случае если автомобиль едет), для полицейских
 автомобилей перед названием автомобиля должно идти слово POLICE;
Для классов TownCar и WorkCar в методе get_status() рядом со значением скорости должна выводиться фраза "ПРЕВЫШЕНИЕ!",
 если скорость превышает 60 (TownCar) и 40 (WorkCar).
Создайте по одному экземпляру каждого производного класса. В цикле из 10 итераций, для каждого автомобиля сделайте
одно из случайных действий: go, stop, turn со случайными параметрами. После каждого действия показывайте статус автомобиля.
'''

import random

class Car:



    def __init__ (self, name= 'mercedez', color= 'Black'):
        self.name = name
        self.color = color
        self.speed = 0
        self.direction = 'straight'



    def go (self, speed):
        self.speed += speed

    def stop (self):
        self.speed = 0


    def turn (self, direction):
        if self.direction == 'straight':
            self.direction = 'back side'
        else:
            self.direction = 'straight'

    def is_police (self):
        return isinstance(self, PoliceCar)

    def get_status(self):
        if (isinstance(self, TownCar) and (self.speed >= 60)) or (isinstance(self, WorkCar) and (self.speed>= 40)):
            print('Марка:{},Цвет:{},Скорость:{} Превышение,Направление:{}'.format(self.name, self.color, self.speed
                                                                                 , self.direction))
        elif isinstance(self, PoliceCar):
            print('Полицейский Марка:{},Цвет:{},Скорость:{},Направление:{}'.format(self.name, self.color, self.speed,
                                                                      self.direction))
        else:
            print('Марка:{},Цвет:{},Скорость:{},Направление:{}'.format(self.name, self.color, self.speed,
                                                                                 self.direction))

class TownCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.speed = 0
        self.direction = 'straight'


class SportCar(Car):

    def __init__(self,name, color):
        super().__init__(name, color)
        self.speed = 0
        self.direction = 'straight'

class WorkCar(Car):

    def __init__(self,name, color):
        super().__init__(name, color)
        self.speed = 0
        self.direction = 'straight'

class PoliceCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.speed = 0
        self.direction = 'straight'

def do_some_action(car):
    if random.randrange(1, 4) == 1:
        car.go(random.randrange(10, 31))
    elif random.randrange(1, 4) == 2:
        car.stop()
    else:
        car.turn(car.direction)
    car.get_status()

police=PoliceCar('Лада', 'Белый')
town=TownCar('BMW', 'Красный')
work=WorkCar('Белаз', 'Серый')
sport=SportCar('Mercedez', 'Чёрный')
for i in range(10):
    do_some_action(police)
    do_some_action(town)
    do_some_action(work)
    do_some_action(sport)