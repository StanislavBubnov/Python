# 2)	Для списка реализовать обмен значений соседних элементов, т.е.
#     Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
#     Для заполнения списка элементов необходимо использовать функцию input().

my_list=[]
new_list = []
len_list = int(input('Введите количество элементов в списке:  '))
i = 0
while len_list != i:
    i += 1
    my_list.append(input('Введите новый элемент списка:  '))
print(my_list)
a = 0
b = len(my_list) % 2
if b == 0:
    while len(my_list) != len(new_list):
        new_list.append(my_list[a+1])
        new_list.append(my_list[a])
        a += 2
else:
    c = my_list.pop()
    while len(my_list) != len(new_list):
        new_list.append(my_list[a+1])
        new_list.append(my_list[a])
        a += 2
    new_list.append(c)
print(new_list)