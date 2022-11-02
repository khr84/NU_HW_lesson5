import os
import sys
from dir_functions import get_list_dir, work_with_dir, write_list_dir_file
from victory import game_victory
from account import account_function

while True:
    print('\n1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр рабочей директории')
    print('5. Просмотр папок рабочей директории')
    print('6. Просмотр файлов рабочей директории')
    print('7. Сохранить содержимое рабочей папки в файл')
    print('8. Просмотр информации об ОС')
    print('9. Создатель программы')
    print('10. Играть в викторину')
    print('11. Мой банковский счет')
    print('12. Выход')

    choise = input('Выберите пункт меню: ')

    if choise == '1':
        work_with_dir('create')
    elif choise == '2':
        work_with_dir('delete')
    elif choise == '3':
        work_with_dir('copy')
    elif choise == '4':
        print(get_list_dir())
    elif choise == '5':
        print(get_list_dir('dir'))
    elif choise == '6':
        print(get_list_dir('file'))
    elif choise == '7':
        write_list_dir_file()
    elif choise == '8':
        print('My OS is', sys.platform, '(', os.name, ')')
    elif choise == '9':
        print('автор: Хуснутдинов Роман (KHR84)')
    elif choise == '10':
        game_victory()
    elif choise == '11':
        account_function()
    elif choise == '12':
        break
    else:
        print('Введен неверный пункт')