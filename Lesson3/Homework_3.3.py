# 3)	Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x,y,z):
    my_list = [x,y,z]
    return sum(my_list)-min(my_list)

x = int(input('Введите число X: '))
y = int(input('Введите число Y: '))
z = int(input('Введите число Z: '))

print(f'Сумма двух ваших наибольших чисел: {my_func(x,y,z)}')