import check as ch
import interface as ie


def search_contact_by_name():

    """
    Функция осуществляет поиск контакта по имени и выводит на печать строки с совпадениями
    """
    name = ie.get_name()
    count = 0
    with open('data.csv', 'r', encoding='utf-8') as file:
        found_contact = []
        for line in file:
            if name in line:                
                count = count + 1
                found_contact.append(line.rstrip('\n'))    
    if count == 0:
        ie.error_no_contact()
    return found_contact 
    
    

def search_contact_by_surname():

    """
    Функция осуществляет поиск контакта по ФИО и выводит на печать строки с совпадениями
    """
    surname = ie.get_surname()
    count = 0
    found_contact = []
    with open('data.csv', 'r', encoding='utf-8') as file:
        for line in file:
            if surname in line:                
                count = count + 1
                found_contact.append(line.rstrip('\n'))
    if count == 0:
        ie.error_no_contact()
    return found_contact

def search_contact_by_phone_num():
    """
    Функция осуществляет поиск контакта по номеру телефона или по имени и выводит на печать строки с совпадениями
    """
    tel_num = ie.get_tel_num()
    count = 0
    found_contact = []
    with open('data.csv', 'r', encoding='utf-8') as file:
        for line in file:
            if tel_num in line:                
                count = count + 1
                found_contact.append(line.rstrip('\n'))
    if count == 0:
        ie.error_no_contact()
    return found_contact

def search_contact_return_number_line(data_contact='иванов'):
    """
    Функция осуществляет поиск контакта по ФИО или по номеру телефона и возвращает номер строки в файле 
    Returns:
    (int)line_number
    """
    count = 0
    line_number=0
    with open('data.csv', 'r', encoding='utf-8') as file:
        for line in file:            
            if data_contact in line:                
                #print(line)
                count = line_number
                return count
            line_number+=1    
    if count == 0:
        return -1
    return count
