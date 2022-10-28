import os.path
from datetime import datetime
import json

def get_sum(str, input_str):
    while not str.isdigit():
        str = input(input_str)
    return (int(str))

def write_file(dict_to_file, file_name):
    with open(file_name, 'a') as f:
        json_to_file = json.dumps(dict_to_file)
        f.write(f'{json_to_file}\n')
def read_sum_file():
    if not os.path.exists(os.path.join(os.getcwd(), 'account.json')):
        now = datetime.now()
        write_file({'date': now.strftime("%d/%m/%Y %H:%M:%S"), 'sum': 0}, 'account.json')
        return(0)
    else:
        f_list = []
        with open('account.json', 'r') as f:
            for line in f:
                f_list.append(line)
        f_str = json.loads(f_list[-1])
        return(f_str['sum'])

def account_function():
    # sum_account = 0
    sum_account = read_sum_file()
    list_buy = []
    while True:

        print('\n1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню: ')
        now = datetime.now()

        if choice == '1':
            sum_add = get_sum('', 'Введите сумму пополнения: ')
            sum_account += sum_add
            list_buy.append((now.strftime("%d/%m/%Y %H:%M:%S"), sum_add, 'пополнение'))
        elif choice == '2':
            sum_buy = get_sum('', 'Введите сумму покупки: ')
            if sum_buy > sum_account:
                print('Не достаточно средств на счете')
                continue
            else:
                sum_account -= sum_buy
                str = input('Введите категорию покупки (12 символов): ')[:12]
                list_buy.append((now.strftime("%d/%m/%Y %H:%M:%S"), -sum_buy, str))
        elif choice == '3':
            print(f'{" " * 15}Дата|{" " * 3}Категория|{" " * 5}Сумма|')
            for date_buy, category, sum_buy in list_buy:
                print(f'{date_buy:19}|{category:>12}|{sum_buy:10}|')
            print(f'Сумма доступных средств = {sum_account}')
        elif choice == '4':
            write_file({'date':now.strftime("%d/%m/%Y %H:%M:%S"), 'sum':sum_account}, 'account.json')
            for date_buy, category, sum_buy in list_buy:
                write_file({'date': date_buy, 'category': category, 'sum': sum_buy}, 'buy_list.json')
            break
        else:
            print('Неверный пункт меню')