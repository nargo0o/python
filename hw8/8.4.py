'''Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет
базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники'''


class StoreOfficeEquipment:
    def __init__(self, name, count, price):
        self.name = name
        self.count = count
        self.price = price


class Printer(StoreOfficeEquipment):
    @property
    def print(self):
        return f'Печать листов'


class Scanner(StoreOfficeEquipment):
    @property
    def scan(self):
        return f'Сканирование листов'


class Xerox(StoreOfficeEquipment):
    @property
    def copy(self):
        return f'Копирование листов'


a = Printer('HP', 2, 2300)
print(a.print)
b = Scanner('HP', 2, 2300)
print(b.scan)
c = Xerox('HP', 2, 2300)
print(c.copy)




