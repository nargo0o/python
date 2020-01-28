''' Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани. Проверить на практике полученные
на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''


class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def calc_coat(self):
        return f' Для пальто: {self.size / 6.5 + 0.5}'

    def calc_suit(self):
        return f'Для костюма: {2 * self.height + 0.3}'

    @property
    def calc_full(self):
        return f'Общий расход ткани: {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}'


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        # self.calc_coat = f'Для пальто: {self.size / 6.5 + 0.5}'

    def calc_coat(self):
        return f'Для пальто: {self.size / 6.5 + 0.5}'


class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        # self.calc_suit = f'Для костюма: {2 * self.height + 0.3}'

    def calc_suit(self):
        return f'Для костюма: {2 * self.height + 0.3}'


coat = Coat(42, 0)
suit = Suit(0, 170)
print(coat.calc_full)
print(coat.calc_coat())
print(suit.calc_suit())

