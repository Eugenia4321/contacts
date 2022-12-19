from interface import get_new_surname
from interface import get_new_name
from interface import get_new_tel_num
from interface import get_new_comment
from interface import get_surname
from interface import get_name
from interface import get_tel_num
from interface import get_comment
from interface import question_to_add
from interface import create_success
from interface import error_surname
from interface import error_name
from interface import error_tel_num
from interface import error_comment
from check import Check_telephon_number
from check import Check_name
from check import Check_comment
import log as lg


def record_in_book():
   """
     Функция осуществляет ввод данных от пользователя
     Returns:
     pohone_book - файл с данными
   """
   with open('data.csv', 'a', encoding='utf-8') as file:
      sur_name = get_surname()
      while Check_name(sur_name) == False:
         error_surname()
         sur_name = get_new_surname()
      else:
         surname = sur_name
      name_chek = get_name()
      while Check_name(name_chek) == False:
         error_name()
         name_chek = get_new_name()
      else:
         name = name_chek
      tel_num = get_tel_num()
      while Check_telephon_number(tel_num) == False:
         error_tel_num()
         tel_num = get_new_tel_num()
      else:
         tel = str(tel_num)
      comment = get_comment()
      while Check_comment(comment) == False:
         error_comment()
         comment = get_new_comment()
      else:
         comment = comment
      data = surname + '|' + name + '|' + tel + '|' + comment
      file.write('\n' + data)
      
      lg.create_log(data, 'log.txt', 'Добавить запись')
      answer = question_to_add().upper()
      if answer == 'Y' or answer == "ДА":
         record_in_book()
      else:
         create_success()
      return data

