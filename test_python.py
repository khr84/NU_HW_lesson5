import math

def test_filter():
    numbers = [1, 2, 3, 4, 5, 25, 46, 78, 34]
    string = ['aa', 'dfa', 'fgh', 'pol', 'erast', 'opliu', 'popl']
    assert list(filter(lambda x: x % 2 == 0, numbers)) == [2, 4, 46, 78, 34]
    assert list(filter(lambda x: x ** 2 in numbers, numbers)) == [1 ,2 ,5]
    assert list(filter(lambda x: 'a' in x, string)) == ['aa', 'dfa', 'erast']
    assert list(filter(lambda x: len(x) == 3, string)) == ['dfa', 'fgh', 'pol']

def test_map():
    numbers = [1, 2, 3, 4, 5, 25, 46, 78, 34]
    string = ['aa', 'dfa', 'fgh', 'pol', 'erast', 'opliu', 'popl']
    assert list(map(lambda x: x ** 2, numbers)) == [1, 4, 9, 16, 25, 625, 2116, 6084, 1156]
    assert list(map(lambda x: x - 10, numbers)) == [-9, -8, -7, -6, -5, 15, 36, 68, 24]
    assert list(map(lambda x: x + 18, numbers)) == [19, 20, 21, 22, 23, 43, 64, 96, 52]
    assert list(map(lambda x: x[0], string)) == ['a', 'd', 'f', 'p', 'e', 'o', 'p']
    assert list(map(lambda x: x[::-1], string)) == ['aa', 'afd', 'hgf', 'lop', 'tsare', 'uilpo', 'lpop']

def test_sorted():
    numbers = [1, 2, 3, 4, 5, 25, 46, 78, 34]
    string = ['aa', 'dfa', 'fgh', 'pol', 'erast', 'opliu', 'popl']
    tuple_list = [(2, 2), (3, 4), (4, 1), (1, 3)]
    assert sorted(numbers) == [1, 2, 3, 4, 5, 25, 34, 46, 78]
    assert sorted(numbers, key = lambda x: x % 5) == [5, 25, 1, 46, 2, 3, 78, 4, 34]
    assert sorted(string) == ['aa', 'dfa', 'erast', 'fgh', 'opliu', 'pol', 'popl']
    assert sorted(string, key = len) == ['aa', 'dfa', 'fgh', 'pol', 'popl', 'erast', 'opliu']
    assert sorted(string, key = lambda x: x[-1], reverse = True) == ['opliu', 'erast', 'pol', 'popl', 'fgh', 'aa', 'dfa']
    assert sorted(tuple_list, key = lambda x: x[1]) == [(4, 1), (2, 2), (1, 3), (3, 4)]

def test_math_pi():
    # формула расчета pi по алгоритму Чудновского
    #   k += ((-1) ** i) * math.factorial(6 * i) * (13591409 + 545140134 * i) / (math.factorial(3 * i) * (math.factorial(i) ** 3) * 640320 ** (3 * i + 3 / 2))
    # k = 1 / (12 * k)
    # возьмем частный случай i == 0
    k = 1 / (12 * (13591409) / (640320 ** (3 / 2)))
    assert math.pi - k < 0.1 * (10 ** -12)
    assert round(math.pi, 5) == 3.14159

def test_math_sqrt():
    assert abs(math.sqrt(5) ** 2 - 5) < 0.1 * (10 ** -12)
    assert abs(math.sqrt(37) ** 2 - 37) < 0.1 * (10 ** -12)
    assert math.sqrt(12) == 12 ** (1/2)
    assert math.sqrt(625) == 25

def test_math_pow():
    assert math.pow(9, 3) == 729
    assert math.pow(3, 3) == 27
    assert math.pow(2, 10) == 1024

def test_math_hypot():
    assert math.hypot(3, 4) == 5
    assert math.hypot(6, 12) == math.sqrt(180)
    assert math.hypot(5, 15) == 250 ** (1/2)
