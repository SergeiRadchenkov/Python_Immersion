'''
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Если ФИО не соответствует условию, выведите:
ФИО должно состоять только из букв и начинаться с заглавной буквы
○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:
Предмет {Название предмета} не найден
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
В противном случае выведите:
Оценка должна быть целым числом от 2 до 5
Результат теста должен быть целым числом от 0 до 100
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета
и по оценкам всех предметов вместе взятых.
Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.
Математика,Физика,История,Литература
Создайте класс Student, который будет представлять студента и его успехи по предметам.
Класс должен иметь следующие методы:
Атрибуты класса:

name (str): ФИО студента. subjects (dict): Словарь,
который хранит предметы в качестве ключей и информацию об оценках
и результатах тестов для каждого предмета в виде словаря.

Магические методы (Dunder-методы):

__init__(self, name, subjects_file): Конструктор класса.
Принимает имя студента и файл с предметами и их результатами.
Инициализирует атрибуты name и subjects и вызывает метод load_subjects для загрузки предметов из файла.

__setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name.
Убеждается, что name начинается с заглавной буквы и состоит только из букв.

__getattr__(self, name):
Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.

__str__(self): Возвращает строковое представление студента, включая имя и список предметов.
Студент: Иван Иванов
Предметы: Математика, История

Методы класса:

load_subjects(self, subjects_file): Загружает предметы из файла CSV.
Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects.

add_grade(self, subject, grade): Добавляет оценку по заданному предмету.
Убеждается, что оценка является целым числом от 2 до 5.

add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету.
Убеждается, что результат теста является целым числом от 0 до 100.

get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.

get_average_grade(self): Возвращает средний балл по всем предметам.
'''
import csv


class Student:
    def __init__(self, name: str, subjects_file):
        self.name = name
        self.subjects = {}
        self.valid_subjects = set()
        self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        if name == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        raise AttributeError(f'Предмет {name} не найден')

    def load_subjects(self, subjects_file):
        with open(subjects_file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                for subject in row:
                    self.valid_subjects.add(subject)

    def add_grade(self, subject, grade):
        if subject in self.valid_subjects:
            if subject not in self.subjects:
                self.subjects[subject] = {'grades': [], 'test_score': []}
            if isinstance(grade, int) and 2 <= grade <= 5:
                self.subjects[subject]['grades'].append(grade)
            else:
                raise ValueError('Оценка должна быть целым числом от 2 до 5')
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def add_test_score(self, subject, score):
        if subject in self.valid_subjects:
            if subject not in self.subjects:
                self.subjects[subject] = {'grades': [], 'test_score': []}
            if isinstance(score, int) and 0 <= score <= 100:
                self.subjects[subject]['test_score'].append(score)
            else:
                raise ValueError('Результат теста должен быть целым числом от 0 до 100')
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def get_average_test_score(self, subject):
        if subject in self.valid_subjects:
            test_scores = self.subjects[subject]['test_score']
            if test_scores:
                return sum(test_scores) / len(test_scores)
            else:
                return 0
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def get_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            total_grades.extend(self.subjects[subject]['grades'])
        if total_grades:
            return sum(total_grades) / len(total_grades)
        else:
            return 0


    def __str__(self):
        full_name = self.name
        subjects = ', '.join(self.subjects.keys())
        return f'Студент: {full_name}\nПредметы: {subjects}'

student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)

