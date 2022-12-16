
def search_contact_by_name():
    
   """
       Функция осуществляет поиск контакта по ФИО или по имени
       и выводит на печать строки с совпадениями
        Returns:
           
    """
   count = 0
   family = input('\nВведите фамилию или имя абонента: ').title()
   with open('data.csv', 'r', encoding='utf-8') as file:
        print("---"*20)
        print('Фамилия|\tИмя|\tНомер_Телефона|\tКомментарий| ')
        print("---"*20)  
        for line in file:

            if family in line:                
                print(line)
                count = count + 1
   if count == 0:
        print('У вас в книги нет абонента с данной фамилией!')
  
   


def search_contact_by_phone_num():
    
   """
       Функция осуществляет поиск контакта по номеру телефона или по имени
       и выводит на печать строки с совпадениями
        Returns:
           
    """
   count = 0
   phone_number = input('Введите номер телефона: ').replace(" ", "")
   with open('data.csv', 'r', encoding='utf-8') as file:
        print("---"*20)
        print('Фамилия|\tИмя|\tНомер_Телефона|\tКомментарий| ')
        print("---"*20)  
        for line in file:

            if phone_number in line:                
                print(line)
                count = count + 1
   if count == 0:
        print('У вас в книги нет абонента с таким номером')

# здесь еще нужно ссылки на проверки.  

