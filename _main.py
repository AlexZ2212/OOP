student_list = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lec_grades(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __avg(self):
        avg = 0
        for key, values in self.grades.items():
            avg = avg + values[0]
        return round(avg / self.grades.items().__len__(), 1)

    def __str__(self):
        res = f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {Student.__avg(self)} \n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)} \n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.__avg() < other.__avg()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __avg(self):
        avg = 0
        for key, values in self.grades.items():
            avg = avg + values[0]
        return round(avg / self.grades.items().__len__(), 1)

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за лекции: {Lecturer.__avg(self)} \n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.__avg() < other.__avg()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n'
        return res

def avg_all_student(course):
    avg = 0

    for key, value in student_list:
        while course in student_list:
            if key == course:
                avg += value
            return
        return

    # while course in student_list:
    #     for key, value in Student.grades.items():
    #         if key == course:
    #             avg += value
    #         return
    #     return
    return avg / len(Student.student_list)

best_student = Student('Ruoy', 'Eman', 'm')

best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['JS']
best_student.courses_in_progress += ['Java']

best_student.finished_courses += ['Git']
student_list.append(best_student)

other_student = Student('Jake', 'Park', 'm')

other_student.courses_in_progress += ['Python']
other_student.courses_in_progress += ['JS']
other_student.courses_in_progress += ['Java']

other_student.finished_courses += ['Git']
student_list.append(other_student)

cool_lecturer = Lecturer('Ed', 'Rien')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['JS']
cool_lecturer.courses_attached += ['Java']

second_lecturer = Lecturer('Devid', 'King')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['JS']
second_lecturer.courses_attached += ['Java']

cool_reviwer = Reviewer('Rin', 'Yamaoki')
cool_reviwer.courses_attached += ['Python']

second_reviwer = Reviewer('Herman', 'Carter')
second_reviwer.courses_attached += ['JS']

cool_reviwer.rate_hw(other_student, 'Python', 6)
cool_reviwer.rate_hw(other_student, 'JS', 10)
cool_reviwer.rate_hw(other_student, 'Java', 5)

cool_reviwer.rate_hw(best_student, 'Python', 7)
cool_reviwer.rate_hw(best_student, 'JS', 8)
cool_reviwer.rate_hw(best_student, 'Java', 9)

best_student.lec_grades(cool_lecturer, 'Python', 10)
best_student.lec_grades(cool_lecturer, 'JS', 9)
best_student.lec_grades(cool_lecturer, 'Java', 10)

best_student.lec_grades(second_lecturer, 'Python', 9)
best_student.lec_grades(second_lecturer, 'JS', 7)
best_student.lec_grades(second_lecturer, 'Java', 5)

print(best_student)
print(other_student)
print(cool_lecturer)
print(second_lecturer)
print(cool_reviwer)
print(second_reviwer)
print(other_student.__lt__(best_student))
print(cool_lecturer.__lt__(second_lecturer))
print(avg_all_student('Python'))
