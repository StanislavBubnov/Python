# 1)	Создать список и заполнить его элементами различных типов данных.
#     Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
#     Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list=[]
numbers = int(input('Введите количество элементов в списке:  '))
i = 0
while i < numbers:
    i += 1
    type_elements = (input('Выбирете тип элемента для ввода(s-строка, i-число, l-list, t-tuple):  '))
    if type_elements == 's':
        elements = input('Введите элемент списка:  ')
        my_list.append(elements)
    elif type_elements == 'i':
        elements = int(input('Введите элемент списка:  '))
        my_list.append(elements)
    elif type_elements == 'l':
        elements = input('Введите элемент списка:  ')
        split_elements = elements.split()
        my_list.append(split_elements)
    elif type_elements == 't':
        elements = input('Введите элемент списка:  ')
        split_elements = elements.split()
        elements_tuple = tuple(split_elements)
        my_list.append(elements_tuple)
print(my_list)

len_my_list = len(my_list)
i = 0
while i < len_my_list:
    print (type(my_list[i]))
    i += 1

