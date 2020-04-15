# 3)	Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

my_list_less20 = []
my_list_salaries = []

with open('test_for_hometask_5.3.txt','r') as my_text:
    my_list = my_text.readlines()
    for i in my_list:
        my_line = i.strip().split(' ')
        my_list_salaries.append(float(my_line[1]))
        if float((my_line[1])) < 20000:
            my_list_less20.append(my_line[0])

print(f'Фамилии сотрудников, которые имеют доход меньше 20 тысяч: {my_list_less20}')
print(f'Средняя велечина дохода сотрудников составляет: {sum(my_list_salaries)/len(my_list):.2f}')

