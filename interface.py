from colorama import init
init()
from colorama import Fore, Back, Style
import check as ch
import create as cr
import delete as de
import find as fd
import format as ft
import log as lg
import read as rd
import update as up

def hello():
    '''Функция приветствия'''
    print(Fore.CYAN + Style.NORMAL + 'Вас приветствует телефонная книга' + Style.RESET_ALL)

def main_menu():
    '''
    Функция главного меню. Возвращает номер пункта меню, который ввёл пользователь.
    '''
    print(Fore.CYAN + Style.NORMAL + '\nМЕНЮ' + Style.RESET_ALL)
    print(Fore.GREEN + Style.NORMAL + '1. Добавить запись' + Style.RESET_ALL)
    print(Fore.BLUE + Style.NORMAL + '2. Найти номер по фамилии' + Style.RESET_ALL)
    print(Fore.BLUE + Style.NORMAL + '3. Найти номер по имени' + Style.RESET_ALL)
    print(Fore.BLUE + Style.NORMAL + '4. Поиск по номеру телефона' + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.NORMAL + '5. Показать все контакты' + Style.RESET_ALL)
    print(Fore.YELLOW + Style.NORMAL + '6. Редактировать запись' + Style.RESET_ALL)
    print(Fore.RED + Style.NORMAL + '7. Удалить запись' + Style.RESET_ALL)
    print(Fore.WHITE + Style.NORMAL + '8. Выйти из программы\n' + Style.RESET_ALL)
    n = int(input(Fore.CYAN + Style.NORMAL + 'Выберите пункт из меню: ' + Style.RESET_ALL))
    return n

def menu_item_1():
    '''
    Функция пункта 1 главного меню. Возвращает результат работы функции создания записи.
    '''
    surname = input(Fore.CYAN + Style.NORMAL + 'Введите фамилию: ' + Style.RESET_ALL).title()[:20]
    name = input(Fore.CYAN + Style.NORMAL + 'Введите имя: ' + Style.RESET_ALL).title()
    number = input(Fore.CYAN + Style.NORMAL + 'Введите номер телефона: ' + Style.RESET_ALL).replace(" ", "")
    comment = input(Fore.CYAN + Style.NORMAL + 'Введите комментарий: ' + Style.RESET_ALL).title()[:40]
    add_contact = cr.record_in_book(surname, name, number, comment) # функция создания записи
    lg.create_log(add_contact, 'log.txt', 'Добавить запись') # функция логирования

def menu_item_2():
    '''
    Функция пункта 2 главного меню. Возвращает результат работы функции поиска контакта по фамилии.
    '''
    find = input(Fore.CYAN + Style.NORMAL + 'Введите фамилию: ' + Style.RESET_ALL).title()
    find_contact = fd.search_contact_by_name(find) # функция поиска контакта по фамилии/имени
    print(find_contact)
    lg.create_log(find_contact, 'log.txt', 'Найти номер по фамилии') # функция логирования

def menu_item_3():
    '''
    Функция пункта 3 главного меню. Возвращает результат работы функции поиска контакта по имени.
    '''
    find = input(Fore.CYAN + Style.NORMAL + 'Введите имя: ' + Style.RESET_ALL).title()
    find_contact = fd.search_contact_by_name(find) # функция поиска контакта по фамилии/имени
    print(find_contact)
    lg.create_log(find_contact, 'log.txt', 'Найти номер по имени') # функция логирования

def menu_item_4():
    '''
    Функция пункта 4 главного меню. Возвращает результат работы функции поиска контакта по номеру.
    '''
    find = input(Fore.CYAN + Style.NORMAL + 'Введите номер  телефона: ' + Style.RESET_ALL).replace(" ", "")
    find_contact = fd.search_contact_by_phone_num(find) # функция поиска контакта по номеру
    lg.create_log(find_contact, 'log.txt', 'Поиск по номеру телефона') # функция логирования

def menu_item_5():
    '''
    Функция пункта 5 главного меню. Возвращает результат работы функции чтения справочника.
    '''
    read_contact = rd.Read_csvfile('data.csv') # функция чтения справочника
    lg.create_log(read_contact, 'log.txt', 'Показать все контакты') # функция логирования

def menu_item_6():
    '''
    Функция пункта 6 главного меню. Печатает предлагаемые опции.
    '''
    print(Fore.BLUE + Style.NORMAL + '1. Найти номер по имени' + Style.RESET_ALL)
    print(Fore.BLUE + Style.NORMAL + '2. Найти номер по фамилии' + Style.RESET_ALL)
    print(Fore.BLUE + Style.NORMAL + '3. Поиск по номеру телефона' + Style.RESET_ALL)
    option = int(input(Fore.CYAN + Style.NORMAL + 'Введите номер пункта: ' + Style.RESET_ALL))
    return option

def menu_item_6_option_1(): # доделать функцию update
    '''
    Функция опции 1 пункта 6 главного меню. Возвращает результат работы функции редактирования записи.
    '''
    find = input(Fore.CYAN + Style.NORMAL + 'Введите фамилию: ' + Style.RESET_ALL)
    print(Fore.CYAN + Style.NORMAL + f'Найденные контакты по фамилии {find}:' + Style.RESET_ALL)
    print(fd.search_contact_by_name(find)) # функция поиска контакта по фамилии/имени
    n_name = input(Fore.CYAN + Style.NORMAL + 'Введите новое имя: ' + Style.RESET_ALL)
    n_surname = input(Fore.CYAN + Style.NORMAL + 'Введите новую фамилию: ' + Style.RESET_ALL)
    n_number = input(Fore.CYAN + Style.NORMAL + 'Введите новый номер телефона: ' + Style.RESET_ALL)
    n_comment = input(Fore.CYAN + Style.NORMAL + 'Введите новый комментарий: ' + Style.RESET_ALL)
    update_contact = up.function_update(find, new_surname=n_surname, new_name=n_name, new_number=n_number, new_comment=n_comment) # функция редактирования записи
    # print(Fore.GREEN + Style.NORMAL + 'Данные успешно изменены' + Style.RESET_ALL)
    lg.create_log(update_contact, 'log.txt', 'Поиск по номеру телефона') # функция логирования


def menu_item_6_option_2(): # доделать функцию update
    '''
    Функция опции 2 пункта 6 главного меню. Возвращает результат работы функции редактирования записи.
    '''
    find = input(Fore.CYAN + Style.NORMAL + 'Введите имя: ' + Style.RESET_ALL)
    print(Fore.CYAN + Style.NORMAL + f'Найденные контакты по фамилии {find}:' + Style.RESET_ALL)
    print(fd.search_contact_by_name(find)) # функция поиска контакта по фамилии/имени
    n_name = input(Fore.CYAN + Style.NORMAL + 'Введите новое имя: ' + Style.RESET_ALL)
    n_surname = input(Fore.CYAN + Style.NORMAL + 'Введите новую фамилию: ' + Style.RESET_ALL)
    n_number = input(Fore.CYAN + Style.NORMAL + 'Введите новый номер телефона: ' + Style.RESET_ALL)
    n_comment = input(Fore.CYAN + Style.NORMAL + 'Введите новый комментарий: ' + Style.RESET_ALL)
    update_contact = up.function_update(find, new_surname=n_surname, new_name=n_name, new_number=n_number, new_comment=n_comment) # функция редактирования записи
    # print(Fore.GREEN + Style.NORMAL + 'Данные успешно изменены' + Style.RESET_ALL)
    lg.create_log(update_contact, 'log.txt', 'Поиск по номеру телефона') # функция логирования

def menu_item_6_option_3(): # доделать функцию update
    '''
    Функция опции 3 пункта 6 главного меню. Возвращает результат работы функции редактирования записи.
    '''
    find = input(Fore.CYAN + Style.NORMAL + 'Введите номер телефона: ' + Style.RESET_ALL)
    print(Fore.CYAN + Style.NORMAL + f'Найденные контакты по номеру телефона {find}:' + Style.RESET_ALL)
    print(fd.search_contact_by_phone_num(find)) # функция поиска контакта по номеру телефона
    n_name = input(Fore.CYAN + Style.NORMAL + 'Введите новое имя: ' + Style.RESET_ALL)
    n_surname = input(Fore.CYAN + Style.NORMAL + 'Введите новую фамилию: ' + Style.RESET_ALL)
    n_number = input(Fore.CYAN + Style.NORMAL + 'Введите новый номер телефона: ' + Style.RESET_ALL)
    n_comment = input(Fore.CYAN + Style.NORMAL + 'Введите новый комментарий: ' + Style.RESET_ALL)
    update_contact = up.function_update(find, new_surname=n_surname, new_name=n_name, new_number=n_number, new_comment=n_comment) # функция редактирования записи
    # print(Fore.GREEN + Style.NORMAL + 'Данные успешно изменены' + Style.RESET_ALL)
    lg.create_log(update_contact, 'log.txt', 'Поиск по номеру телефона') # функция логирования

# когда будем связывать опции для 6 пункта меню, в конце не забыть проверку:
# else:
#     print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

def menu_item_7():
    '''
    Функция пункта 7 главного меню. Печатает предлагаемые опции.
    '''
    print(Fore.BLUE + Style.NORMAL + '1. Найти номер по фамилии' + Style.RESET_ALL)
    print(Fore.BLUE + Style.NORMAL + '2. Найти номер по имени' + Style.RESET_ALL)
    print(Fore.BLUE + Style.NORMAL + '3. Поиск по номеру телефона' + Style.RESET_ALL)
    option = input(Fore.CYAN + Style.NORMAL + 'Введите номер пункта: ' + Style.RESET_ALL)
    return option

def menu_item_7_option_1():
    '''
    Функция опции 1 пункта 7 главного меню. Возвращает результат работы функции удаления записи.
    '''
    find = input(Fore.CYAN + Style.NORMAL + 'Введите фамилию: ' + Style.RESET_ALL)
    print(Fore.CYAN + Style.NORMAL + f'Найденные контакты по фамилии {find}:' + Style.RESET_ALL)
    print(fd.search_contact_by_name(find)) # функция поиска контакта по фамилии/имени
    delete_contact = de.delete_contact(data_list = 0, name_data_list = "data.csv", id_delete_contact = 5) # откуда брать аргументы для функции?
    lg.create_log(delete_contact, 'log.txt', 'Поиск по номеру телефона') # функция логирования

def menu_item_7_option_2():
    '''
    Функция опции 2 пункта 7 главного меню. Возвращает результат работы функции удаления записи.
    '''
    find = input(Fore.CYAN + Style.NORMAL + 'Введите имя: ' + Style.RESET_ALL)
    print(Fore.CYAN + Style.NORMAL + f'Найденные контакты по имени {find}:' + Style.RESET_ALL)
    print(fd.search_contact_by_name(find)) # функция поиска контакта по фамилии/имени
    delete_contact = de.delete_contact(data_list = 0, name_data_list = "data.csv", id_delete_contact = 5) # откуда брать аргументы для функции?
    lg.create_log(delete_contact, 'log.txt', 'Поиск по номеру телефона') # функция логирования
  
def menu_item_7_option_3():
    '''
    Функция опции 3 пункта 7 главного меню. Возвращает результат работы функции удаления записи.
    '''
    find = input(Fore.CYAN + Style.NORMAL + 'Введите имя: ' + Style.RESET_ALL)
    print(Fore.CYAN + Style.NORMAL + f'Найденные контакты по имени {find}:' + Style.RESET_ALL)
    print(fd.search_contact_by_name(find)) # функция поиска контакта по номеру телефона
    delete_contact = de.delete_contact(data_list = 0, name_data_list = "data.csv", id_delete_contact = 5) # откуда брать аргументы для функции?
    lg.create_log(delete_contact, 'log.txt', 'Поиск по номеру телефона') # функция логирования

# когда будем связывать опции для 7 пункта меню, в конце не забыть проверку:
# else:
#     print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

def menu_item_8():
    '''
    Функция пункта 8 главного меню. Завершает работу телефонного справочника.
    '''
    print(Fore.CYAN + Style.NORMAL + 'Спасибо за работу!' + Style.RESET_ALL)

# когда будем связывать пункты меню, в конце не забыть проверку:
# else:
#     print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


# menu_item_1() # проверено
# menu_item_2() # проверено
# menu_item_3() # проверено
# menu_item_4() # проверено
# menu_item_5() # проверено
# menu_item_6() # проверено
# menu_item_6_option_1() # доделать функцию update
# menu_item_6_option_2() # доделать функцию update
# menu_item_6_option_3() # доделать функцию update
# menu_item_7() # проверено
# menu_item_7_option_1() # обсудить аргументы функции, пока проверка невозможна
# menu_item_7_option_2() # обсудить аргументы функции, пока проверка невозможна
# menu_item_7_option_3() # обсудить аргументы функции, пока проверка невозможна
# menu_item_8() # проверено

# если в функциях проверок описать только логику, а сообщения перенести в интерфейс: обсудить:
# def checking_tel_num(tel_num: str):
#     '''Вызываем функцию проверки номера телефона из модуля check'''
#     while True:
#         print(Fore.CYAN + Style.NORMAL + 'Введите номер телефона: ' + Style.RESET_ALL)
#         if ch.check_telephone_number(tel_num) == False: # если вводят не числа/ длина <= 13
#             print(Fore.RED + Style.NORMAL + 'Введён неверный номер телефона' + Style.RESET_ALL)
#         else:
#             print(Fore.GREEN + Style.NORMAL + 'Номер введён верно' + Style.RESET_ALL)

# def checking_name(name: str):
#     '''Вызываем функцию проверки имени из модуля check'''
#     while True:
#         print(Fore.CYAN + Style.NORMAL + 'Введите имя: ' + Style.RESET_ALL)
#         if ch.check_name(name) == False: # если вводят не буквы/ длина больше 40 символов
#             print(Fore.RED + Style.NORMAL + 'Имя введено некорректно. Попробуйте снова: ' + Style.RESET_ALL)
#         else:
#             print(Fore.GREEN + Style.NORMAL + 'Имя введено верно' + Style.RESET_ALL)

# def checking_surname(surname: str):
#     '''Вызываем функцию проверки фамилии из модуля check'''
#     while True:
#         print(Fore.CYAN + Style.NORMAL + 'Введите фамилию: ' + Style.RESET_ALL)
#         if ch.check_name(surname) == False: # если вводят не буквы/ длина больше 40 символов
#             print(Fore.RED + Style.NORMAL + 'Фамилия введена некорректно. Попробуйте снова: ' + Style.RESET_ALL)
#         else:
#             print(Fore.GREEN + Style.NORMAL + 'Фамилия введена верно' + Style.RESET_ALL)

# def checking_comment(comment: str):
#     '''Вызываем функцию проверки комментария из модуля check'''
#     while True:
#         print(Fore.CYAN + Style.NORMAL + 'Введите комментарий: ' + Style.RESET_ALL)
#         if ch.check_comment(comment) == False: # если ввели больше 300 символов
#             print(Fore.RED + Style.NORMAL + 'Превышен лимит в 300 символов. Попробуйте снова: ' + Style.RESET_ALL)
#         else:
#             print(Fore.GREEN + Style.NORMAL + 'Комментарий введён верно' + Style.RESET_ALL)
