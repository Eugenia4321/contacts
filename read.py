def read_cont():
    print("---"*20)
    print('Фамилия|\tИмя|\tНомер_Телефона|\tКомментарий| ')
    print("---"*20)
    with open('data.csv', 'r', encoding='utf-8') as file:
        for line in file:
            import_cont = line.split(',')
            print('\t\t\t'.join(import_cont),end='')
    print('\n')


import csv
def read_cont2():
    with open("data.csv", encoding='utf-8') as file:
        # Создаем объект DictReader, указываем символ-разделитель ","
        file_reader = csv.DictReader(file, delimiter = "|")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'Файл содержит столбцы: \n{"       ".join(row)}')
            # Вывод строк
            print(f' {row["Фамилия"]} \t {row["Имя"]}\t {row["Телефон"]} \t{row["Комментарий"]}\n' , end='')
            count += 1
        print(f'Всего в файле {count + 1} строк.')
 
#Оба способа выводят на печать не красиво в случае если имя или фамилия длинные.


#  Еще две функции для чтения, чтобы посмотреть, какая лучше подойдет для проекта.

def Read_csvfile(datacsv): 
    """чтение cvs файла и вывод на экран"""
    import csv
    with open(datacsv, encoding='utf-8') as data:
        file_reader = csv.reader(data, delimiter = "|")
        count = 0
        for row in file_reader:
            if count == 0:
                    # Вывод строки, содержащей заголовки для столбцов
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                    # Вывод строк
                print(f' {row[0]} {row[1]} {row[2]}.')
            count += 1

print(Read_csvfile("data.csv"))

def Read_csvfile_for_list(datacsv) ->list: 
    """чтение cvs файла и запись в список"""
    import csv
    data_list = []
    with open(datacsv, encoding='utf-8') as data:
        file_reader = csv.reader(data, delimiter = "|")

        for row in file_reader:
                   data_list.append(row)
    return data_list

print(Read_csvfile_for_list("data.csv"))
