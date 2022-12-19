def Check_telephon_number(tel_num: str): 
    """Проверка номера телефона"""
    if tel_num.isdigit() and len(tel_num)==11:
        return True
    else:
        return False 

def Check_name(name: str): 
    """Проверка имени или фамилии"""
    if name.isalpha() and 2 <= len(name) <= 40:
        return True
    else:
        return False 

def Check_comment(comment: str): 
    """Проверка комментария"""
    if 2 <= len(comment) <= 301:
        return True
    else:
        return False   
