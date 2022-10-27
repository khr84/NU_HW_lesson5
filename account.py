from datetime import datetime

def get_sum(str, input_str):
    while not str.isdigit():
        str = input(input_str)
    return (int(str))

def add_buy(sum, category='пополнение'):
    now = datetime.now()
    return((now.strftime("%d/%m/%Y %H:%M:%S"), category, sum))


def account_function():
    sum_account = 0
    list_buy = []
    while True:

        print('\n1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню: ')

        if choice == '1':
            sum_add = get_sum('', 'Введите сумму пополнения: ')
            sum_account += sum_add
            list_buy.append(add_buy(sum_add))
        elif choice == '2':
            sum_buy = get_sum('', 'Введите сумму покупки: ')
            if sum_buy > sum_account:
                print('Не достаточно средств на счете')
                continue
            else:
                sum_account -= sum_buy
                str = input('Введите категорию покупки (12 символов): ')[:12]
                list_buy.append(add_buy(-sum_buy, str))
        elif choice == '3':
            print(f'{" " * 15}Дата|{" " * 3}Категория|{" " * 5}Сумма|')
            for date_buy, category, sum_buy in list_buy:
                print(f'{date_buy:19}|{category:>12}|{sum_buy:10}|')
            print(f'Сумма доступных средств = {sum_account}')
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')