'''Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.'''

def salary():
    try:
        time = int(input('Отработанное время: '))
        pay_h = float(input('Ставка в час: '))
        bonus = float(input('Премия: '))
        return (time * pay_h) + bonus
    except ValueError:
        return None
calc = salary()
print(f'Заработная плата в этом месяце: {calc}')
