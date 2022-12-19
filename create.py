from interface import get_surname
from interface import get_name
from interface import get_tel_num
from interface import get_comment
from interface import create_success
import log as lg


def record_in_book():
   """
     Функция осуществляет ввод данных от пользователя
     Returns:
     pohone_book - файл с данными
   """
   with open('data.csv', 'a', encoding='utf-8') as file:
      surname = get_surname()
      name = get_name()
      tel_num = get_tel_num()
      tel = str(tel_num)
      comment = get_comment()
      data = surname + '|' + name + '|' + tel + '|' + comment
      file.write('\n' + data)
      lg.create_log(data, 'log.txt', 'Добавить запись')
      create_success()
      return data

