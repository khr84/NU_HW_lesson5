import os
import shutil

def get_list_dir(data = ''):
    list_dir = os.listdir()
    result = []
    if data == 'file':
        for element in list_dir:
            if os.path.isfile(os.path.join(os.getcwd(), element)):
                result.append(element)
        return(result)
    elif data == 'dir':
        for element in list_dir:
            if os.path.isdir(os.path.join(os.getcwd(), element)):
                result.append(element)
        return (result)
    else:
        return(list_dir)

def write_list_dir_file():
    with open('listdir.txt', 'w') as f:
        for element in ['file','dir']:
            list_dir = get_list_dir(element)
            list_dir.sort()
            if element == 'file':
                str_begin = 'files:'
            else:
                str_begin = '\ndirs:'
            str_list_dir = str_begin + ''.join(map(lambda x: f' {x},', list_dir)).rstrip(',')
            f.write(str_list_dir)

def del_path(path_del):
    path_del_type = ''
    if os.path.isfile(path_del):
        path_del_type = 'файл'
        os.remove(path_del)
    elif os.path.isdir(path_del):
        path_del_type = 'папка'
        shutil.rmtree(path_del)
    return(path_del_type)

def copy_path(path_from, path_to):
    path_copy_type = ''
    if os.path.isfile(path_from):
        path_copy_type = 'файл'
        # копируем файл в указанную директорию
        shutil.copy(path_from, path_to)
    elif os.path.isdir(path_from):
        path_copy_type = 'папка'
        # копируем папки в указанную директорию
        shutil.copytree(path_from, path_to)
    return(path_copy_type)

def check_path(path_for_check):
    return(path_for_check[0] in ['\\', '/']  or path_for_check[-1] in ['\\', '/'])

def work_with_dir(work_type):
    path_dir = input('Введите имя папки или файла: ')
    if check_path(path_dir):
        print('Неверно указан путь: разделителя не должно быть в начале или в конце')
    else:
        path_dir = os.path.join(os.getcwd(), path_dir)
        # создание папки
        if work_type == 'create':
            if os.path.exists(path_dir):
                print('Такая папка уже существует')
            else:
                os.makedirs(path_dir)
                print(f'Создана папка {path_dir}')
        # удаление папки/файла
        elif work_type == 'delete':
            if not os.path.exists(path_dir):
                print('Такой папки/файла не существует')
            else:
                path_type = del_path(path_dir)
                print(f'Удален(а) {path_type} {path_dir}')
        # копирование папки/файла
        elif work_type == 'copy':
            if not os.path.exists(path_dir):
                print('Такая папка/файл не существует')
            else:
                path_goal = input('Введите папку/файл куда надо скопировать: ')
                if check_path(path_goal):
                    print('Неверно указан путь: разделителя не должно быть в начале или в конце')
                else:
                    path_goal = os.path.join(os.getcwd(), path_goal)
                    if os.path.isdir(path_dir) and os.path.exists(path_goal):
                        print(f'Уже существуют объект {path_goal}')
                    elif os.path.isfile(path_dir) and path_dir == path_goal:
                        print('Нельзя скопировать файл в самого себя')
                    elif not os.path.exists(os.path.split(path_goal)[0]):
                        print(f'Не существует целевой папки {os.path.split(path_goal)[0]}')
                    else:
                        path_type = copy_path(path_dir, path_goal)
                        print(f'{path_type} {path_dir} скопирован(а) в {path_goal}')