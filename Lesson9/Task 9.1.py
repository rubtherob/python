'''Создать класс TrafficLight (светофор).
определить у него один приватный атрибут color (цвет) и метод get_current_signal() (получить текущий цвет);
после создания экземпляра светофора, он запускает режим смены сигналов с разной длительностью: красный (3 сек),
 жёлтый (1 сек), зелёный (3 сек);
переключение идет циклично в порядке красный-жетлый-зеленый-красный-жетлый-зеленый-красный-...
проверить переключение режимов работы светофора, опрашивая в цикле текущее состояние светофора с интервалом 0.5 секунды,

 используя метод get_current_signal().'''

import datetime
import time

class TrafficLight:

    def __init__(self):
        _color= 'red'



    def get_current_signal(self, obj):
        print(obj)
        time.sleep(0.5)



    def start(self):
        timer = int(time.clock())
        while True:
            timer = int(time.clock())
            if timer % 7 < 3:
                _color='red'
                self.get_current_signal(_color)
            elif timer % 7 >= 3 and timer % 7< 4:
                _color = 'yellow'
                self.get_current_signal(_color)
            elif timer % 7 <= 7:
                _color = 'green'
                self.get_current_signal(_color)


trafficlight = TrafficLight()
trafficlight.start()

