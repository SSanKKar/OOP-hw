class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lt(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades_for_lectures:
                lecturer.grades_for_lectures[course].append(rate)
            else:
                lecturer.grades_for_lectures[course] = [rate]

    def average_grade_hw(self):
        all_grades = 0
        all_courses = 0

        for grades in self.grades.values():
            all_grades += sum(grades)
            all_courses += len(grades)
        return all_grades / all_courses if all_courses > 0 else 0

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade_hw() == other.average_grade_hw()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade_hw() < other.average_grade_hw()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade_hw() > other.average_grade_hw()
        return NotImplemented

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade_hw()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_for_lectures = {}

    def average_grades_lecturer(self):
        all_grades = 0
        all_courses = 0

        for grades in self.grades_for_lectures.values():
            all_grades += sum(grades)
            all_courses += len(grades)
        return all_grades / all_courses if all_courses > 0 else 0

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grades_lecturer() == other.average_grades_lecturer()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grades_lecturer() < other.average_grades_lecturer()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grades_lecturer() > other.average_grades_lecturer()
        return NotImplemented

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades_lecturer()}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

student_1 = Student('Kolya', 'Ivanov', 'Man')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Java']

student_2 = Student('Nikita', 'Semenov', 'Man')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Java', 'Git']

reviewer_1 = Reviewer('Kostya', 'Fomin')

reviewer_2 = Reviewer('Stepan', 'Bilkin')

lecturer_1 = Lecturer('Oleg', 'Stepanov')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Eugen', 'Morozov')
lecturer_2.courses_attached += ['Git']

student_1.rate_lt(lecturer_1, 'Python', 4)
student_2.rate_lt(lecturer_2, 'Git', 7)

reviewer_1.rate_hw(student_1, 'Git', 5)
reviewer_2.rate_hw(student_2, 'Python', 8)

print(student_1)
print()
print(student_2)
print()
print(reviewer_1)
print()
print(reviewer_2)
print()
print(lecturer_1)
print()
print(lecturer_2)