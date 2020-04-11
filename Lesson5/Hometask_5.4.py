# 4)	Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

my_list_2 = []

with open('test_for_hometask_5.4(1).txt','r') as my_text:
    my_list = my_text.readlines()
    for i in my_list:
        a = i.strip().split(' ')
        if a[0] == 'One':
            a[0] = 'Один'
        if a[0] == 'Two':
            a[0] = 'Два'
        if a[0] == 'Three':
            a[0] = 'Три'
        if a[0] == 'Four':
            a[0] = 'Четыре'
        my_list_2.append(a)

with open('test_for_hometask_5.4(2).txt','w+') as my_text:
    for i in my_list_2:
        my_text.write(' '.join(i))
        my_text.write('\n')