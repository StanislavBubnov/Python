# 2)	Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('test_for_hometask_5.2.txt','r') as my_text:
    my_list = my_text.readlines()
    my_text.seek(0)
    print(f'Количество строк в файле: {len(my_list)}')
    for ind, el in enumerate(my_list):
        my_line = len(el.strip().split(' '))
        print(f'В строке {ind+1} количество слов равно: {my_line}, а символов в строке: {len(el.strip())} ')
