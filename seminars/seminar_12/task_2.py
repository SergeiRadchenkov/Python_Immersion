'''
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
'''
import json


class Factorial:
    def __init__(self, limit: int):
        self.limit = limit
        self.storage = {}

    def _fact(self, num: int):
        factorial = []
        number = 1
        for i in range(1, num + 1):
            number *= i
            factorial.append(number)
        return factorial

    def __call__(self, number: int):
        result = self._fact(number)[-self.limit:]
        self.storage[number] = result
        return result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        file = open('fact_dict.json', 'w', encoding='utf-8')
        json.dump(self.storage, file, indent=4)
        file.close()


with Factorial(4) as fact:
    print(fact(20))
    print(fact(5))
    print(fact(10))
    print(fact(7))
    print(fact(100))
