'''
Возьмите любые 1-3 задания из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.
'''
import csv
import logging
import argparse
import os

logging.basicConfig(filename='student.log', filemode='a', encoding='utf-8', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Student:
    def __init__(self, name: str, subjects_file):
        self.name = name
        self.subjects = {}
        self.valid_subjects = set()
        self.subjects_file = subjects_file
        self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        if name == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                logging.error('Ошибка: ФИО должно состоять только из букв и начинаться с заглавной буквы')
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        logging.error(f'Предмет {name} не найден')
        raise AttributeError(f'Предмет {name} не найден')

    def load_subjects(self, subjects_file):
        try:
            with open(subjects_file, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    subject = row[0]
                    if "Тесты:" in row:
                        index = row.index("Тесты:")
                        grades = list(map(int, row[1:index]))
                        test_scores = list(map(int, row[index + 1:]))
                    else:
                        grades = list(map(int, row[1:]))
                        test_scores = []
                    self.subjects[subject] = {'grades': grades, 'test_score': test_scores}
                    self.valid_subjects.add(subject)
                logging.info(f'Загружены предметы: {self.valid_subjects}')
        except Exception as e:
            logging.error(f'Ошибка при загрузке предметов из файла: {e}')
            raise

    def update_subjects_file(self):
        with open(self.subjects_file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for subject, data in self.subjects.items():
                # Записываем предмет, оценки и тестовые результаты в CSV
                row = [subject] + data['grades'] + ["Тесты:"] + data['test_score']
                writer.writerow(row)
        logging.info(f'Файл {self.subjects_file} обновлен')

    def add_grade(self, subject, grade):
        try:
            if subject not in self.valid_subjects:
                # Добавляем новый предмет, если его нет
                self.subjects[subject] = {'grades': [], 'test_score': []}
                self.valid_subjects.add(subject)
                logging.info(f'Добавлен новый предмет: {subject}')
            if isinstance(grade, int) and 2 <= grade <= 5:
                self.subjects[subject]['grades'].append(grade)
                logging.info(f'Добавлена оценка {grade} по предмету {subject}')
            else:
                logging.error('Ошибка: Оценка должна быть целым числом от 2 до 5')
                raise ValueError('Оценка должна быть целым числом от 2 до 5')
        except Exception as e:
            logging.error(f'Ошибка при добавлении оценки: {e}')
            raise

        self.update_subjects_file()

    def add_test_score(self, subject, score):
        try:
            if subject in self.valid_subjects:
                if isinstance(score, int) and 0 <= score <= 100:
                    self.subjects[subject]['test_score'].append(score)
                    logging.info(f'Добавлен результат теста {score} по предмету {subject}')
                else:
                    logging.error('Ошибка: Результат теста должен быть целым числом от 0 до 100')
                    raise ValueError('Результат теста должен быть целым числом от 0 до 100')
            else:
                logging.error(f'Ошибка: Предмет {subject} не найден')
                raise ValueError(f'Предмет {subject} не найден')
        except Exception as e:
            logging.error(f'Ошибка при добавлении результата теста: {e}')
            raise

        self.update_subjects_file()

    def get_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            total_grades.extend(self.subjects[subject]['grades'])
        if total_grades:
            return sum(total_grades) / len(total_grades)
        else:
            return 0

    def get_average_test_score(self, subject):
        try:
            if subject in self.valid_subjects:
                test_scores = self.subjects[subject]['test_score']
                if test_scores:
                    return sum(test_scores) / len(test_scores)
                else:
                    return 0
            else:
                logging.error(f'Ошибка: Предмет {subject} не найден')
                raise ValueError(f'Предмет {subject} не найден')
        except Exception as e:
            logging.error(f'Ошибка при вычислении среднего результата теста: {e}')
            raise

    def __str__(self):
        full_name = self.name
        subjects = ', '.join(self.subjects.keys())
        return f'Студент: {full_name}\nПредметы: {subjects}'


def main():
    parser = argparse.ArgumentParser(description="Управление информацией о студенте")
    parser.add_argument("name", type=str, help="ФИО студента")
    parser.add_argument("subjects_file", type=str, help="CSV файл с перечнем предметов")
    parser.add_argument("--add-grade", nargs=2, metavar=('subject', 'grade'), help="Добавить оценку")
    parser.add_argument("--add-test-score", nargs=2, metavar=('subject', 'score'),
                        help="Добавить результат теста")
    parser.add_argument("--get-average-grade", action='store_true', help="Получить средний балл")
    parser.add_argument("--get-average-test-score", metavar='subject',
                        help="Получить средний результат теста по предмету")

    args = parser.parse_args()

    student = Student(args.name, args.subjects_file)

    if args.add_grade:
        subject, grade = args.add_grade
        student.add_grade(subject, int(grade))

    if args.add_test_score:
        subject, score = args.add_test_score
        student.add_test_score(subject, int(score))

    if args.get_average_grade:
        print(f"Средний балл: {student.get_average_grade()}")

    if args.get_average_test_score:
        subject = args.get_average_test_score
        print(f"Средний результат по тестам по предмету {subject}: {student.get_average_test_score(subject)}")

    print(student)


if __name__ == "__main__":
    main()


'''
Примеры запуска в консоле:

python HW_task_1.py "Иван Иванов" "subjects.csv"
python HW_task_1.py "Иван Иванов" "subjects.csv" --add-grade "Математика" 4
python HW_task_1.py "Иван Иванов" "subjects.csv" --add-test-score "История" 85 
python HW_task_1.py "Иван Иванов" "subjects.csv" --get-average-grade
python HW_task_1.py "Иван Иванов" "subjects.csv" --get-average-test-score "Математика"
'''