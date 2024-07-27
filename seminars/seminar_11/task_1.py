"""
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
"""
from datetime import datetime


class MyStr(str):
    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.create_time = datetime.now()

        return instance

    # def __init__(self, author, value):
    #     self.author = author
    #     self.value = value
    #     self.create_time = time()


a = MyStr('Это моя строка', 'Sergei')
print(a)
print(a.author)
print(a.create_time)
