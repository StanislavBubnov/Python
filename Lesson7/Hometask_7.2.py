class Clothes:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    @property
    def my_method(self):
        my_coat = (self.param_1 / 6.5 + 0.5)
        my_costume = round((2 * self.param_2 + 0.3)/100,2)
        return f'Параметры, переданные в класс: \nРазмер: {self.param_1}, Рост: {self.param_2} \n'\
            f'На пальто нужно {my_coat} м. ткани, на костюм {my_costume} м ткани \n'\
            f'Всего ткани нужно {my_coat + my_costume} метров'


my_clothes = Clothes(52,182)
print(my_clothes.my_method)