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


def work_with_dir(work_type):
    path_dir = input('Введите имя папки или файла: ')
    if path_dir[0] in ['\\', '/']  or path_dir[-1] in ['\\', '/']:
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
                if os.path.isfile(path_dir):
                    os.remove(path_dir)
                    print(f'Удален файл {path_dir}')
                elif os.path.isdir(path_dir):
                    shutil.rmtree(path_dir)
                    print(f'Удалена папка {path_dir}')
        # копирование папки/файла
        elif work_type == 'copy':
            if not os.path.exists(path_dir):
                print('Такая папка/файл не существует')
            else:
                path_goal = input('Введите папку/файл куда надо скопировать: ')
                if path_goal[0] in ['\\','/'] or path_goal[-1] in ['\\','/']:
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
                        if os.path.isfile(path_dir):
                            shutil.copy(path_dir, path_goal)
                            print(f'Файл {path_dir} скопирован в {path_goal}')
                        elif os.path.isdir(path_dir):
                            # копируем папки в указанную директорию
                            shutil.copytree(path_dir, path_goal)
                            print(f'Папка {path_dir} скопирована в {path_goal}')
