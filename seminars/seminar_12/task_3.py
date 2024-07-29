'''
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
'''


class Factorial:
    def __init__(self, start: int = 1, stop: int = 1, step: int = 1):
        self.start = start
        self.stop = stop
        self.step = step
        self._value = self._fact()

    def _fact(self):
        result = []
        number = 1
        for i in range(self.start, self.stop, self.step):
            number *= i
            result.append(number)
        return result

    def __iter__(self):
        return self

    def __next__(self):
        while self._value:
            return self._value.pop(0)
        raise StopIteration

a = Factorial(5)
for i in a:
    print(i)
