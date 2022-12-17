import csv
import find as fd

def function_update(find, new_surname='', new_name='', new_number='', new_comment=''):
    # with open('data.csv', 'w', encoding = 'utf-8', newline='') as csv_phonebook:
    #     csv_writer = csv.writer(csv_phonebook, delimiter = '|', lineterminator="\r")
        line = list(str(fd.search_contact_by_name(find)).split('|'))
        for _ in line:
            if(new_surname != ''):
                line[0] = new_surname.title()

            if(new_name != ''):
                line[1] = new_name.title()

            if(new_number != ''):
                line[2] = new_number.replace(" ", "")

            if(new_comment != ''):
                line[3] = new_comment.lower()
        print(line) # ищем в справочнике строку, меняем в ней старые данные на новые

# как теперь новую строку вписать на место старой в файл???
