import os
import shutil
from datetime import datetime
from account import add_buy
from dir_functions import check_path, del_path, copy_path

def test_add_buy():
    now = datetime.now()
    assert add_buy(100) == (now.strftime("%d/%m/%Y %H:%M:%S"), 'пополнение', 100)
    assert add_buy(-200, 'food') == (now.strftime("%d/%m/%Y %H:%M:%S"), 'food', -200)
    assert add_buy(1000, 'game') == (now.strftime("%d/%m/%Y %H:%M:%S"), 'game', 1000)

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