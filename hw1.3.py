#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = int(input('Введите число n: '))
nn = str(n + n)
nnn = str(n + n + n)
print(str(n)+nn+nnn)
