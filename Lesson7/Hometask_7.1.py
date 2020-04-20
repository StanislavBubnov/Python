class Matrix:
    def __init__(self, my_list = []):
        self.my_list = my_list
    def __str__(self):
        str_1 = ' '.join(str(e) for e in self.my_list[0])
        str_2 = ' '.join(str(e) for e in self.my_list[1])
        str_3 = ' '.join(str(e) for e in self.my_list[2])
        return '|{}|\n|{}|\n|{}|'.format(str_1,str_2,str_3)
    def __add__(self, other):
        str_1 = [a + b for a, b in zip(self.my_list[0], other.my_list[0])]
        str_2 = [a + b for a, b in zip(self.my_list[1], other.my_list[1])]
        str_3 = [a + b for a, b in zip(self.my_list[2], other.my_list[2])]
        return Matrix([str_1,str_2,str_3])



matrix_a = Matrix([[1,4,5],[6,7,9], [4,7,3]])
print(matrix_a)

print('~'*150)

matrix_b = Matrix([[7,-3,5],[2,-1,9], [2,-2,3]])
print(matrix_b)
print('~'*150)

print(matrix_a+matrix_b)