'''
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
'''
from string import ascii_lowercase

def clear_text(text: str):
    result = ''
    for i in text:
        if i.lower() in ascii_lowercase + ' ':
            result += i
    return result.lower()


print(clear_text('testText777'))
