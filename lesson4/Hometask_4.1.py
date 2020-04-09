from sys import argv

script_name, first_param, second_param, third_param = argv



print('Program name', script_name)


print('Hello')
print('Working hours:  ', first_param)
print('Cost for 1 hour:  ', second_param)
print('Prize:  ', third_param)
wage = int(first_param) * int(second_param) + int(third_param)
print('Wage:', wage)