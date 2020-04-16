# 4)	Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#     А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#     Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#     Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#     Для классов TownCar и WorkCar переопределите метод show_speed.
#     При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self,name,speed,color,is_police=None):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self):
        print('Машина развернулась')
    def show_speed(self):
        print(f'Скорость машины: {self.speed}')
    def check_police(self):
        print('Это полицейская машина') if self.is_police == True else print('Это не полицейская машина')

class TownCar(Car):
    def show_speed(self):
        print('Превышение скорости!') if self.speed > 60 else print(f'Скорость машины: {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print('Превышение скорости!') if self.speed > 40 else print(f'Скорость машины: {self.speed}')

class PoliceCar(Car):
    def __init__(self,name,speed,color,is_police=None):
        super().__init__(name,speed,color,is_police=True)


my_car = TownCar('Rover',70,'black')
print(my_car.name)
print(my_car.speed)
print(my_car.color)
my_car.go()
my_car.stop()
my_car.turn()
my_car.show_speed()
my_car.check_police()
print('~'*150)

my_sportcar = SportCar('Ferrari',120,'red')
print(my_sportcar.name)
print(my_sportcar.speed)
print(my_sportcar.color)
my_sportcar.go()
my_sportcar.stop()
my_sportcar.turn()
my_sportcar.show_speed()
my_sportcar.check_police()
print('~'*150)

bus = WorkCar('Nefaz',50,'yellow')
print(bus.name)
print(bus.speed)
print(bus.color)
bus.go()
bus.stop()
bus.turn()
bus.show_speed()
bus.check_police()
print('~'*150)

police = PoliceCar('Лада',80,'white')
print(police.name)
print(police.speed)
print(police.color)
police.go()
police.stop()
police.turn()
police.show_speed()
police.check_police()