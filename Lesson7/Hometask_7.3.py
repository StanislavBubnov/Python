class Cell:
    def __init__(self, param_1):
        self.param_1 = param_1
    def __add__(self, other):
        return self.param_1 + other.param_1
    def __str__(self):
        return str(self.param_1)
    def __sub__(self, other):
        return self.param_1 - other.param_1 if self.param_1 > other.param_1 else 'Разность клеток меньше 0!'
    def __mul__(self, other):
        return self.param_1 * other.param_1
    def __truediv__(self, other):
        return self.param_1 // other.param_1
    def make_order(self,param_2):
        while self.param_1 > param_2:
            print(param_2 * '*')
            self.param_1 = self.param_1 - param_2
        print(self.param_1 * '*')


cell_1 = Cell(380)
cell_2 = Cell(99)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

cell_3 = Cell(15)
cell_3.make_order(6)