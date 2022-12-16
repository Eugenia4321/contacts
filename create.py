def record_in_book():

   """
       Функция осуществляет ввод данных от пользователя
        Returns:
           pohone_book - файл с данными
    """
   with open('data.csv', 'a', encoding='utf-8') as file:
        family = input('Введите фамилию: ').title()[:20]
        name = input('Введите имя: ').title()
        tel = input('Введите номер телефона: ').replace(" ", "")
        for _ in str(tel):
            if tel[0] != '+' or tel[1] != '7':
                print('Номер должен начинаться "+7" и содержать 12 символов. Введите номер заново')
                tel = input('Введите номер телефона: ').replace(" ", "")
        if len(tel) != 12:
                print('Проверьте правильность ввода номера. Номер телефона должен содержать 12 символов')
                tel = input('Введите номер телефона: ').replace(" ", "")
        comment = input('Введите комментарий ').title()[:40]
        data = family + '|' + name + '|' + tel + '|' + comment
        file.write('\n' + data)
        answer = input('Хотите ввести еще один контакт? ')
        print(answer)
        if answer == 'да':
            record_in_book()
        else:
            print('Контакт успешно создан.')
        return data
# здесь еще нужно ссылки на проверки.


