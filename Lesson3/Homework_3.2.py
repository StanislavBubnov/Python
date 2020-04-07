# 2)	Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def my_contacts(name,surname,date_birthday,city,email,phone):
    print(f'Имя: {name},Фамимлия: {surname},Дата др: {date_birthday},Город: {city},email: {email},Телефон: {phone}')

my_contacts(name='Stas',surname='Bubnov',date_birthday='28.10.90',city='Krasnoyarsk',email='bubnovstnislav@gmail.com',phone='8967126636')