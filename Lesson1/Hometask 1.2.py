# 2)Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_seconds=int(input('Введите время в секундах: '))

hours=user_seconds//3600
minutes=user_seconds//60
minutes_in_clock=user_seconds//60-hours*60
seconds_in_clock=user_seconds-minutes*60
print(f'Ваше время в формате чч:мм:сс составляет: {hours}:{minutes_in_clock}:{seconds_in_clock}')