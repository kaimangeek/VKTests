import pytest


# Тесты Float
def test_float_one():
    result = 1
    try:
        a = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
        assert result == a
    except AssertionError:
        pass


@pytest.mark.parametrize("test_input,expected", [(3.03 + 5, 8.03), (2.1 * 2, 4.2), (8.4 / 4, 2.1)])
def test_float_two(test_input, expected):
    assert (test_input) == expected


# Тесты list
testsList = [([1, 2, 3], 2), ([7, 8, 9], 8), ([4, 5, 6], 5)]


@pytest.mark.parametrize('mas, x', testsList)
def test_list_one(mas, x):
    res = mas.pop(1)
    assert x == res


def test_list_two():
    result = [1, 2, 3]
    try:
        result.remove(4)
    except ValueError:
        pass


# Тесты tuple

testsList = [('Hello', ('H', 'e', 'l', 'l', 'o')), ('VK', ('V', 'K')),
             ('take', ('t', 'a', 'k', 'e')), ('me', ('m', 'e')), ('please', ('p', 'l', 'e', 'a', 's', 'e'))]


@pytest.mark.parametrize('mas, x', testsList)
def test_tuple_one(mas, x):
    res = tuple(mas)
    assert x == res


def test_tuple_two():
    result = (1, 2, 3)
    try:
        result.append(4)
    except AttributeError:
        pass