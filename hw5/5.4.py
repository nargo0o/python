'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл. '''



with open('file_4.txt', 'r') as my_file, open('file_4.1.txt', 'w') as my_file_1:
    old_data = my_file.read()
    new_data_0 = old_data.replace('One', 'Один')
    my_file_1.write(new_data_0)
    new_data_1 = old_data.replace('Two', 'Два')
    my_file_1.write(new_data_1)
    new_data_2 = old_data.replace('Three', 'Три')
    my_file_1.write(new_data_2)
    new_data_3 = old_data.replace('Four', 'Четыре')
    my_file_1.write(new_data_3)


