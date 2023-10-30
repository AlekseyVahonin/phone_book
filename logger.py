from data_create import *

def input_data():
    name = input_name()
    surname = input_surname()
    patronymic = input_patronymic()
    phone = input_phone()
    adress = input_adress()
    str_data = f'{name} {surname} {patronymic} {phone} \n{adress}\n\n'
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(str_data)


def read_file():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        return file.read()


def print_data():
    print('='*50, end='\n\n')
    original_file = read_file().rstrip().split('\n\n')
    for index in range(len(original_file)):
        print(f'{index + 1}. {original_file[index]}\n')
    print('='*50)


def search_contact():

    print('Выберите вариант операции:\n'
          '1. Имя: \n'
          '2. Фамилия: \n'
          '3. Отчество: \n'
          '4. Телефон: \n'
          '5. Адрес: ')
    command = input('Введите номер операции: ')

    while command not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод')
        command = input('Введите номер операции: ')

    i_search_param = int(command) - 1

    search = input('Введите параметр: ').title()
    print()
    contacts_list = read_file().rstrip().split('\n\n')

    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        if search in contact_lst[i_search_param]:
            print(contact_str)


def copy_data():
    print_data()
    line = int(input('Выберите строку для копирования: ')) - 1

    original_file = read_file().rstrip().split('\n\n')
    with open('phonebook_copy.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{original_file[line]}\n')


def change_data():

    print('Выберите вариант операции:\n'
          '1. Изменить имя: \n'
          '2. Изменить фамилию: \n'
          '3. Изменить отчество: \n'
          '4. Изменить телефон: \n'
          '5. Изменить адрес: ')
    command = input('Введите номер операции: ')

    while command not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод')
        command = input('Введите номер операции: ')

    i_search_param = int(command) - 1

    search = input('Что изменить: ').title()
    change = input('На что изменить: ').title()
    contacts_list = read_file().rstrip().split('\n\n')

    count = 0
    list_stroka = []
    line = []

    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        if search in contact_lst[i_search_param]:

            contact_lst[i_search_param] = change
            line.append(count)

            stroka = ''
            for index in range(len(contact_lst)):
                if index == 3:
                    stroka += contact_lst[index] + '\n'
                else:
                    stroka += contact_lst[index] + ' '
            list_stroka.append(stroka)
        count += 1

    count_list_stroka = len(list_stroka)

    if count_list_stroka > 0:

        number_line = 0
        if count_list_stroka > 1:
            print('='*50, end='\n\n')
            for index in range(count_list_stroka):
                print(f'{index + 1}. {contacts_list[line[index]]}\n')
            print('='*50)
            number_line = int(
                input('Выберите номер строки для изменения: ')) - 1

        if number_line <= count_list_stroka:
            contacts_list[line[number_line]] = list_stroka[number_line]
            with open('phonebook.txt', 'w', encoding='UTF-8') as file:
                for contact in contacts_list:
                    file.write(f'{contact}\n\n')
        else:
            print()
            print('Не корректный ввод', end='\n')
    else:
        print()
        print('Совпадений не найдено', end='\n')


def delete_data():
    print_data()

    line = int(input('Выберите строку для удаления: ')) - 1
    contacts_list = read_file().rstrip().split('\n\n')
    if len(contacts_list) >= line:
        contacts_list.pop(line)
        with open('phonebook.txt', 'w', encoding='UTF-8') as file:
            for contact in contacts_list:
                file.write(f'{contact}\n\n')
    else:
        print('Некорректный ввод')

