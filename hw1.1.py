#  Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
name = input('Ваше имя?: ')
print(type(name))

mobile_number = int(input('Номер телефона: '))
print(type(mobile_number))

weight = float(input('Ваш вес?: '))
print(type(weight))

print(f' Привет, {name}. Твой номер телефона: {mobile_number}. Ты весишь - {weight} кг.')