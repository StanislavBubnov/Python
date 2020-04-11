# 5)	Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#     Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('test_for_hometask_5.5.txt','w+') as my_text:
        my_text.write(input('Введите Ваши числа через пробел: '))


with open('test_for_hometask_5.5.txt', 'r') as my_text:
        my_list = my_text.read().split()
        print(f'Результат сложения Ваших чисел равен: {sum(list(map(int, my_list)))}')
