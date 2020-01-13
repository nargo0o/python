# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide():
    try:
        a = int(input('Введите число: '))
        b = int(input('Введите число: '))
        number = a / b
        return number
    except ZeroDivisionError:
        return None
    except ValueError:
        return None

result = divide()
print(result)