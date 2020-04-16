# 1)	Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#     Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
#     Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
#     Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
#     Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    def __init__(self,color):
        self.__color = color
    def running(self):
        start_time = time.time()
        time_after_color_1 = 7
        time_after_color_2 = time_after_color_1 + 2
        time_after_color_3 = time_after_color_2 + 10
        i = 0
        print(self._TrafficLight__color[i])
        while time.time() != start_time + time_after_color_1:
            continue
        i += 1
        print(self._TrafficLight__color[i])
        while time.time() != start_time + time_after_color_2:
            continue
        i += 1
        print(self._TrafficLight__color[i])
        while time.time() != start_time + time_after_color_3:
            continue
        print('Цвета светофора корректны') if self._TrafficLight__color == ['red', 'yellow', 'green'] else print('Цвета светофора не корректны')

traffic_1 = TrafficLight(['red', 'yellow', 'green'])
traffic_1.running()

traffic_2 = TrafficLight('white blue black'.split())
traffic_2.running()