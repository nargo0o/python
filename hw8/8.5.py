'''Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное
подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
 любую подходящую структуру, например словарь.'''


class StoreOfficeEquipment:
    def __init__(self, name, count, price):
        self.name = name
        self.count = count
        self.price = price
        self.equip_store = []
        self.res = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.count}

    @property
    def my_method(self):
        try:
            name = input(f'Введите наименование ')
            price = int(input(f'Введите цену за ед '))
            count = int(input(f'Введите количество '))
            result = {'Модель устройства': name, 'Цена за ед': price, 'Количество': count}
            self.res.update(result)
            self.equip_store.append(self.res)
            print(f' Результат: {self.equip_store}')
        except ValueError:
            print('error')


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
a.my_method


