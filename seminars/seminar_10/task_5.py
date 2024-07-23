'''
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
'''


class Dog:
    def __init__(self, name, age, command='run'):
        self.name = name
        self.age = age
        self.command = command

    def show_info_dog(self):
        return (f'{self.name} can {self.command}')


class Cat:
    def __init__(self, name, age, sleep_time):
        self.name = name
        self.age = age
        self.sleep_time = sleep_time

    def show_info_vat(self):
        return (f'{self.name} sleeps {self.sleep_time} hours')


class Bird:
    def __init__(self, name, age, volume):
        self.name = name
        self.age = age
        self.volume = volume

    def show_info_bird(self):
        return (f'{self.name} sing {self.volume} db')


pet1 = Dog('Bob', 5, 'fight')
pet2 = Cat('Felix', 2, 4)
pet3 = Bird('Aro', 1, 3)

print(pet1.show_info_dog())
print(pet2.show_info_vat())
print(pet3.show_info_bird())
