from logger import *

def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass

    command = ''
    while command != '7':
        print('Выберите вариант работы с телефонным справочником:\n'
              '1. Запись данных:\n'
              '2. Выыод данных:\n'
              '3. Поиск данных:\n'
              '4. Копирование данных:\n'
              '5. Изменение данных:\n'
              '6. Удаление данных:\n'
              '7. Выход')
        command = input('Введите номер операции: ')
        while command not in ('1', '2', '3', '4', '5', '6', '7'):
            print('Некорректный ввод')
            command = input('Введите номер операции: ')

        match command:
            case '1':
                input_data()
            case '2':
                print_data()
            case '3':
                search_contact()
            case '4':
                copy_data()
            case '5':
                change_data()
            case '6':
                delete_data()
            case '7':
                print('Выход из программы')