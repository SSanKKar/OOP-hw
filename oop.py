class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lt(self, lecturer, course, rate):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and
            (course in self.courses_in_progress or course in self.finished_courses)):
            if course in lecturer.grades_for_lectures:
                lecturer.grades_for_lectures[course].append(rate)
            else:
                lecturer.grades_for_lectures[course] = [rate]

    def average_grade_hw(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count != 0 else 0

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
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade_hw()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

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
        total = 0
        count = 0
        for grades in self.grades_for_lectures.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count != 0 else 0

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

def average_homework_grade(students, course):
    total_sum = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            grades = student.grades[course]
            total_sum += sum(grades)
            total_count += len(grades)
    return total_sum / total_count if total_count != 0 else 0

def average_lecture_grade(lecturers, course):
    total_sum = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades_for_lectures:
            grades = lecturer.grades_for_lectures[course]
            total_sum += sum(grades)
            total_count += len(grades)
    return total_sum / total_count if total_count != 0 else 0


student_1 = Student('Kolya', 'Ivanov', 'Man')
student_1.courses_in_progress.extend(['Python', 'Git'])
student_1.finished_courses.append('Java')

student_2 = Student('Nikita', 'Semenov', 'Man')
student_2.courses_in_progress.extend(['Python', 'Git'])
student_2.finished_courses.append('Java')

reviewer_1 = Reviewer('Kostya', 'Fomin')
reviewer_1.courses_attached.extend(['Python', 'Git'])

reviewer_2 = Reviewer('Stepan', 'Bilkin')
reviewer_2.courses_attached.extend(['Git', 'Python'])

lecturer_1 = Lecturer('Oleg', 'Stepanov')
lecturer_1.courses_attached.extend(['Python', 'Git'])

lecturer_2 = Lecturer('Eugen', 'Morozov')
lecturer_2.courses_attached.extend(['Git', 'Python'])

student_1.rate_lt(lecturer_1, 'Python', 4)
student_1.rate_lt(lecturer_1, 'Git', 5)
student_2.rate_lt(lecturer_2, 'Git', 7)
student_2.rate_lt(lecturer_2, 'Python', 9)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 2)
reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Python', 9)

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
print()

print(f"Средняя оценка за домашние задания по Python: {average_homework_grade([student_1, student_2], 'Python')}")
print(f"Средняя оценка за лекции по Git: {average_lecture_grade([lecturer_1, lecturer_2], 'Git')}")