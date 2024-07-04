'''
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.

Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того,
как убрали знак препинания апостроф) считать двумя словами.
Цифры за слова не считаем.

Отсортируйте по убыванию значения количества повторяющихся слов.
Слова выведите в обратном алфавитном порядке.
'''
# text = 'Hello world. Hello Python. Hello again.'
# text = 'This is a sample text without repeating words.'
text = "Python 3.9 is the latest version of Python. It's awesome!"

new_text = ''
for item in text:
    if item == "'":
        item = " "
    if item.isalpha() or item.isspace():
        new_text += item.lower()

split_text = new_text.split(" ")

my_dict = dict()
for item in split_text:
    if item != '':
        my_dict[item] = split_text.count(item)

sor = sorted(my_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)

print(sor)

# Вариант 2
import re
from collections import Counter

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]

print(top_words)
