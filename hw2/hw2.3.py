#3 Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
season = ['Зима', 'Весна', 'Лето', 'Осень']

if month == 1 or month == 2 or month == 12:
    print(season[0])
elif month == 3 or month == 4 or month == 5:
    print(season[1])
elif month == 6 or month == 7 or month == 8:
    print(season[2])
elif month == 9 or month == 10 or month == 11:
    print(season[3])

season_dict = {1: 'Зима',
               2: 'Весна',
               3: 'Лето',
               4: 'Осень'
               }
if month == 1 or month == 2 or month == 12:
    print(season_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(season_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(season_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(season_dict.get(4))