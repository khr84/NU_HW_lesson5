import os
import shutil
import json
from dir_functions import get_list_dir, check_path, del_path, copy_path, write_list_dir_file
from account import write_file, read_sum_file

def test_check_path():
    assert check_path('111') == False
    assert check_path('/222') == True
    assert check_path('333\\') == True
    assert check_path('\\lesson\\') == True

def test_del_path():
    path_dir = os.path.join(os.getcwd(), '111')
    os.makedirs(path_dir)
    assert del_path(path_dir) == 'папка'
    path_dir = os.path.join(os.getcwd(), 'text.txt')
    f = open(path_dir, 'tw', encoding='utf-8')
    f.close()
    assert del_path(path_dir) == 'файл'
    assert '111' not in os.listdir(os.getcwd())
    assert 'text.txt' not in os.listdir(os.getcwd())

def test_copy_path():
    # копируем 111 в 222
    os.makedirs(os.path.join(os.getcwd(), '111'))
    assert copy_path(os.path.join(os.getcwd(), '111'), os.path.join(os.getcwd(), '222')) == 'папка'
    assert '222' in os.listdir(os.getcwd())
    assert '111' in os.listdir(os.getcwd())
    # копируем 222 в 333\444
    os.makedirs(os.path.join(os.getcwd(), '333'))
    assert copy_path(os.path.join(os.getcwd(), '222'), os.path.join(os.getcwd(), '333\\444')) == 'папка'
    assert '444' in os.listdir(os.path.join(os.getcwd(), '333'))
    # копируем text.txt в text2.txt
    f = open(os.path.join(os.getcwd(), 'text.txt'), 'tw', encoding='utf-8')
    f.close()
    assert copy_path(os.path.join(os.getcwd(), 'text.txt'), os.path.join(os.getcwd(), 'text2.txt')) == 'файл'
    assert 'text.txt' in os.listdir(os.getcwd())
    assert 'text2.txt' in os.listdir(os.getcwd())
    # копируем text.txt в 333\444\text3.txt
    assert copy_path(os.path.join(os.getcwd(), 'text.txt'), os.path.join(os.getcwd(), '333\\444\\text3.txt')) == 'файл'
    assert 'text3.txt' in os.listdir(os.path.join(os.getcwd(), '333\\444'))
    # удаляем папки/файлы которые создали
    shutil.rmtree(os.path.join(os.getcwd(), '111'))
    shutil.rmtree(os.path.join(os.getcwd(), '222'))
    shutil.rmtree(os.path.join(os.getcwd(), '333'))
    os.remove(os.path.join(os.getcwd(), 'text.txt'))
    os.remove(os.path.join(os.getcwd(), 'text2.txt'))

def test_write_read_file():
    write_file({'test_str':'значение', 'sum': 100}, 'test_write_file.txt')
    assert os.path.exists(os.path.join(os.getcwd(), 'test_write_file.txt'))
    with open('test_write_file.txt', 'r') as f:
        data_str = json.loads(f.read())
        assert data_str == {'test_str':'значение', 'sum': 100}
    assert read_sum_file('test_write_file.txt') == 100
    # delete
    os.remove('test_write_file.txt')

def test_write_list_dir():
    write_list_dir_file()
    assert os.path.exists(os.path.join(os.getcwd(), 'listdir.txt'))
    with open('listdir.txt', 'r') as f:
        for i in range(2):
            str_file = f.readline()
            str_file = str_file.replace('\n', '')
            if i == 0:
                list_dir = get_list_dir('file')
                list_dir.sort()
                assert list_dir == str_file.replace('files: ', '').split(', ')
            elif i == 1:
                list_dir = get_list_dir('dir')
                list_dir.sort()
                assert list_dir == str_file.replace('dirs: ', '').split(', ')
    #delete
    os.remove('listdir.txt')



