# 5)	Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


my_list = [300,200,100,50,40,30,20,20,20,10]
new_num = int(input('Введите новый элемент списка:   '))
if my_list.count(new_num) > 0:
    i = len(my_list) - my_list[::-1].index(new_num)
    my_list.insert(i,new_num)
    print(f'Элемент встает в список с индексом {i}')
elif my_list.pop() > new_num:
    my_list.append(new_num)
else:
    for i, el in enumerate(my_list):
        if el < new_num:
            my_list.insert(i,new_num)
            break
print(my_list)
