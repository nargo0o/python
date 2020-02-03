'''Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
умножение созданных экземпляров. Проверьте корректность полученного результата.'''


class ComplexNumber:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __str__(self):
        return f'x = {self.num_1} + {self.num_2} * i'

    def __add__(self, other):
        return f'Сложение = {self.num_1 + other.num_1} + {self.num_2 + other.num_2} * i'

    def __mul__(self, other):
        return f'Умножение = {(self.num_1 * other.num_1) - (self.num_2 * other.num_2)} + {self.num_2 * other.num_1} * i'


a = ComplexNumber(1, 2)
b = ComplexNumber(2, 1)
print(a)
print(b)
print(a + b)
print(a * b)