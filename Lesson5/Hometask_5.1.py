# 1)	Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#     Об окончании ввода данных свидетельствует пустая строка.

with open('test_for_hometask_5.1.txt','w+') as my_text:
    while True:
        new_line = (input('Введите строку: '))
        my_text.write(new_line)
        my_text.write('\n')
        if new_line == '':
            break
    my_text.seek(0)
    print(my_text.read())
