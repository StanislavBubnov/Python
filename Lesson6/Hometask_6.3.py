# 3)	Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
#     Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#     Создать класс Position (должность) на базе класса Worker.
#     В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#     Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self,name, surname, position, income={'wage':None, 'bonus':None}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return ('Имя сотрудника: {} {}'.format(self.name, self.surname))
    def get_total_income(self):
        return (f'Доход {self.position} равен {sum(self._income.values())}')


position_1 = Position('Sergey','Savin','Economist',{'wage':20000, 'bonus':5000})
print(position_1.name)
print(position_1.surname)
print(position_1.position)
print(position_1._income)
print(position_1.get_full_name())
print(position_1.get_total_income())
print('~'*150)

position_1 = Position('Andrey','Rogov','Bloger',{'wage':35000, 'bonus':0})
print(position_1.name)
print(position_1.surname)
print(position_1.position)
print(position_1._income)
print(position_1.get_full_name())
print(position_1.get_total_income())