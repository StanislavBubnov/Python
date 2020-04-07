# 4)	Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_split(x,y):
    print(x*y)

def my_func_1(x,y):
    if y < 0:
        return abs(x) ** y
    else:
        y *= -1
        return abs(x) ** y

x = int(input('Введите число X: '))
y = int(input('Введите число Y: '))
my_split('-',100)
print(f'Способ 1: X в отрицательной степени Y: {my_func_1(x,y)}')
my_split('-',100)



def my_func_2(x,y,z=1):
    i = 0
    if y < 0:
        while i != y:
            i -= 1
            z = abs(x) * z
        return 1 / z
    else:
        y *= -1
        while i != y:
            i -= 1
            z = abs(x) * z
        return 1 / z

print(f'Способ 2: X в отрицательной степени Y: {my_func_2(x,y)}')
my_split('-',100)

print(f'Проверочная формула: {pow(x,y)}')
my_split('-',100)