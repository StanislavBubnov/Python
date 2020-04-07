# 5)	Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

my_numbers = None
my_list = []

def int_func(my_numbers):
    while True:
        my_numbers = input('Введите Ваши цифры, которые вы хотите сложить через пробел (для окончания введите q):')
        if my_numbers.count('q') != 1:
            my_numbers_split = my_numbers.split()
            for i in my_numbers_split:
                my_list.append(int(i))
            print(f'Ваша последовательность цифр: {my_list}')
            print(f'Сумма Ваших чисел равна: {sum(my_list)}')
        else:
            my_numbers_split = my_numbers.split()
            for i in my_numbers_split:
                my_list.append(i)
            my_list.remove('q')
            print(f'Ваша последовательность цифр: {list(map(int,my_list))}')
            return sum(list(map(int,my_list)))

print(f'Сумма Ваших чисел равна: {int_func(my_numbers)}')
