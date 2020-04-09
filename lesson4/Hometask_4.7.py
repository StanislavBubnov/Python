# 7)	Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
#     При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
#         Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


from itertools import count
from functools import reduce

def generator():
    n = int(input('Введите число, факториал которого вы хотите получить: '))
    for el in count(1):
        if el == n+1:
            break
        yield el

def my_func(num_1, num_2):
    return num_1 * num_2

g = generator()
my_list =[]

for el in g:
    my_list.append(el)
    print(el)

print((my_list))
print(reduce(my_func, my_list))




