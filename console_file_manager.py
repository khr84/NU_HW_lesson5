import os
import sys
from dir_functions import get_list_dir, work_with_dir
from victory import game_victory
from account import account_function

while True:
    print('\n1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр рабочей директории')
    print('5. Просмотр папок рабочей директории')
    print('6. Просмотр файлов рабочей директории')
    print('7. Просмотр информации об ОС')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Выход')

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
        print('My OS is', sys.platform, '(', os.name, ')')
    elif choise == '8':
        print('автор: Хуснутдинов Роман (KHR84)')
    elif choise == '9':
        game_victory()
    elif choise == '10':
        account_function()
    elif choise == '11':
        break
    else:
        print('Введен неверный пункт')