#4)	Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

i=int(input('Введите число n:  '))
a=0
if i>10:
    while i>10:
        b = i % 10
        i //=  10
        if a < b:
            a = b
    if a < i:
        a = i
else:
    a=i
print(f'Самая большая цифра в Вашем числе {a}')