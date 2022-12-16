def Check_telephon_number(tel_num: str): 
    while True:
        if not tel_num.isdigit():
            print("Вы ввели не числа. Попробуйте снова: ")
        elif not 7<= int(tel_num) <= 11:
            print("Ваш номер недействительный. Попробуйте снова")
        else:
            return tel_num


def Check_name(name: str): 
    """Проверка имени или фамилии"""
    while True:
        if not name.isalpha():
            print("Вы ввели не буквы. Попробуйте снова: ")
        elif not 2 <= int(name) <= 40:
            print("Превышен лимит символов. Попробуйте снова")
        else:
            return name


def Check_comment(comment: str): 
    """Проверка комментария"""
    while True:
        if not 2 <= int(comment) <= 301:
            print("Превышен лимит символов. Попробуйте снова")
        else:
            return comment
    
