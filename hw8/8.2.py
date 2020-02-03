'''Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''


class ZeroDivEr:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    @staticmethod
    def divide_method(num_1, num_2):
        try:
            res = num_1 / num_2
            return res
        except ZeroDivisionError:
            return f'Деление на ноль'


a = ZeroDivEr(10, 0)
print(ZeroDivEr.divide_method(2, 0))
print(ZeroDivEr.divide_method(2, 3))
