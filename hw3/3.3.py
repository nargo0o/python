# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    numbers = [a, b, c]
    max_numbers = []
    max_num_1 = max(numbers)
    max_numbers.append(max_num_1)
    numbers.remove(max_num_1)
    max_num_2 = max(numbers)
    max_numbers.append(max_num_2)
    result = max_num_1 + max_num_2
    print(result)
numbers = my_func(2,8,6)
numbers = my_func(9,3,8)
numbers = my_func(1,4,2)
