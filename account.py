import os.path
from datetime import datetime
import json

def get_sum(input_str):
    while True:
        try:
            str_number = int(input(input_str))
        except:
            print('Введено не число')
        else:
            return(int(str_number))
            break

def add_dtime(func):
    def inner(*args, **kwargs):
        with open(args[0], 'a') as f:
            now = datetime.now()
            f.write(f'{{"date":"{now.strftime("%d/%m/%Y %H:%M:%S")}", "data":')
        result = func(*args, **kwargs)
        with open(args[0], 'a') as f:
            f.write(f'}}\n')
        return(result)
    return inner

@add_dtime
def write_file(file_name, dict_to_file):
    with open(file_name, 'a') as f:
        json_to_file = json.dumps(dict_to_file)
        f.write(f'{json_to_file}')
def read_sum_file(file_name):
    if not os.path.exists(os.path.join(os.getcwd(), file_name)):
        write_file(file_name, {'sum': 0})
        return(0)
    else:
        f_list = []
        with open(file_name, 'r') as f:
            for line in f:
                f_list.append(line)
        f_str = json.loads(f_list[-1])
        return(f_str['data']['sum'])

def account_function():
    # sum_account = 0
    sum_account = read_sum_file('account.json')
    list_buy = []
    while True:

        print('\n1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню: ')
        now = datetime.now()

        if choice == '1':
            sum_add = get_sum('Введите сумму пополнения: ')
            sum_account += sum_add
            list_buy.append((now.strftime("%d/%m/%Y %H:%M:%S"), sum_add, 'пополнение'))
            write_file('buy_list.json', {'category': 'пополнение', 'sum': sum_add})
        elif choice == '2':
            sum_buy = get_sum('Введите сумму покупки: ')
            if sum_buy > sum_account:
                print('Не достаточно средств на счете')
                continue
            else:
                sum_account -= sum_buy
                str_category = input('Введите категорию покупки (12 символов): ')[:12]
                list_buy.append((now.strftime("%d/%m/%Y %H:%M:%S"), -sum_buy, str_category))
                write_file('buy_list.json', {'category': str_category, 'sum': -sum_buy})
        elif choice == '3':
            print(f'{" " * 15}Дата|{" " * 3}Категория|{" " * 5}Сумма|')
            for date_buy, sum_buy, category in list_buy:
                print(f'{date_buy:19}|{category:>12}|{sum_buy:10}|')
            print(f'Сумма доступных средств = {sum_account}')
        elif choice == '4':
            write_file('account.json', {'sum':sum_account})
            break
        else:
            print('Неверный пункт меню')