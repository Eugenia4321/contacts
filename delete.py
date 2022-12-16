from log import create_log


def delete_contact(data_list: list,name_data_list: str="data.csv", id_delete_contact: int = 5):
    """ принимает список контактов , название файла с данными и номер строки с контактом для удаления (отсчет с 0 )
    Arguments:
             (list)data_list список контактов где 1 элемент это 'имя|фамилия|номер телефона|комментарий'
             (str)name_data_list- название файла с контактами 
             (int) id_delete_contact - номер записи в файле для удаления (нумерация с 0 строки)
       
    """
    new_data_list = data_list[:id_delete_contact]+data_list[id_delete_contact+1:]
    delete_contact_item = []
    delete_contact_item.append(data_list[id_delete_contact].split('|'))
    #print(f' delete {delete_contact_item}')
    create_log(delete_contact_item)
    with open(name_data_list, "w", encoding='UTF-8') as data_file:
        for i in range(len(new_data_list)):
            data_file.write(f'{new_data_list[i]}\n')
    data_file.close()


