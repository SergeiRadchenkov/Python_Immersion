'''
Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
'''
import doctest
from string import ascii_lowercase

def clear_text(text: str):
    '''
    >>> clear_text('texttexttest') == 'texttexttest'
    True
    >>> clear_text('textText11teSt') == 'texttexttest'
    True
    >>> clear_text('text.Text11teSt') == 'texttexttest'
    True
    >>> clear_text('textTextВАПНРвпол11teSt') == 'texttexttest'
    True
    >>> clear_text('textText,./11teSt') == 'texttexttest'
    True
    '''
    result = ''
    if text is not None:
        for i in text:
            if i.lower() in ascii_lowercase + ' ':
                result += i
        return result.lower()
    raise ValueError('Incorrect')



if __name__ == '__main__':
    doctest.testmod(verbose=True)
