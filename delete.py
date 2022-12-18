from log import create_log
from interface import get_data_contact
from find import search_contact_return_number_line
from read import get_lines_list_of_contacts


def delete_contact(name_data_list: str="data.csv"):
    """ принимает название файла, вызывает функцию поиска по имени или фамилии, удаляет контакт если он найден
    Arguments:
             (str)name_data_list- название файла с контактами        
    """
    data_contact=get_data_contact()
    id_delete_contact=search_contact_return_number_line(data_contact)
    data_list=get_lines_list_of_contacts(name_data_list)
    if id_delete_contact>0:
        new_data_list = data_list[:id_delete_contact]+data_list[id_delete_contact+1:]
        delete_contact_item = []
        delete_contact_item.append(data_list[id_delete_contact].split('|'))
    
        create_log(delete_contact_item)
        with open(name_data_list, "w", encoding='UTF-8') as data_file:
             for i in range(len(new_data_list)):
               data_file.write(f'{new_data_list[i]}')
        data_file.close()
        print(f'Контакт удален!')
    else:
        print(f'Контакт не найден!')   

