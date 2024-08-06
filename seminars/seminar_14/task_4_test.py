'''
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
'''
import pytest
from task_1 import clear_text


def test1():
    assert clear_text('text') == 'text'


def test2():
    assert clear_text('TexT') == 'text'


def test3():
    assert clear_text('Te..xt') == 'text'


def test4():
    assert clear_text('TeЯЯxt') == 'text'


def test5():
    assert clear_text('Te.Я.x.Я.t') == 'text'


if __name__ == '__main__':
    pytest.main(['-v'])
