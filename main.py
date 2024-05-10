class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # функция, с помощью которой студент оценивает лекции:
    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached
                and grade in range(11)):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avergrades(self):
        self.all_grades = sum(list(self.grades.values()), [])
        return round(sum(self.all_grades) / len(self.all_grades), 1)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.avergrades()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершённые курсы: {', '.join(self.finished_courses)}')

    # магические функции сравнения по оценкам за задания:
    def __gt__(self, other):
        return self.avergrades() > other.avergrades()

    def __lt__(self, other):
        return self.avergrades() < other.avergrades()

    def __eq__(self, other):
        return self.avergrades() == other.avergrades()

    def __ne__(self, other):
        return self.avergrades() != other.avergrades()


class Mentor:
    def __init__(self, name, surname, courses_attached):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached, avergrades=None):
        super().__init__(name, surname, courses_attached)
        self.grades = {}

    def avergrades(self):
        self.all_grades = sum(list(self.grades.values()), [])
        return round(sum(self.all_grades) / len(self.all_grades), 1)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.avergrades()}')

    # магические функции сравнения по оценкам за лекции:

    def __gt__(self, other):
        return self.avergrades() > other.avergrades()

    def __lt__(self, other):
        return self.avergrades() < other.avergrades()

    def __eq__(self, other):
        return self.avergrades() == other.avergrades()

    def __ne__(self, other):
        return self.avergrades() != other.avergrades()


class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)

    # функция, с помощью которой проверяющий оценивает домашние работы:

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress
                and grade in range(11)):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


# студенты:
student_list = []

student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.add_courses('Введение в программирование')
student_list.append(student1)

student2 = Student('Jane', 'Abc', 'female')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Введение в программирование']
student2.add_courses('Git')
student_list.append(student2)

# лекторы:
lecturers_list = []

lecturer1 = Lecturer('Michael', 'Bcd', [])
lecturer1.courses_attached += ['Git']
lecturer1.courses_attached += ['Python']
lecturers_list.append(lecturer1)

lecturer2 = Lecturer('Anna', 'Cde', [])
lecturer2.courses_attached += ['Python']
lecturers_list.append(lecturer2)

# проверяющие:

reviewer1 = Reviewer('John', 'Buddy', [])
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Git']

reviewer2 = Reviewer('Kate', 'Opq', [])
reviewer2.courses_attached += ['Введение в программирование']

# реализация методов выставления оценок:

# проверяющие выставляют оценки студентам:

reviewer1.rate_hw(student1, 'Python', 6)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Введение в программирование', 10)
reviewer2.rate_hw(student2, 'Введение в программирование', 7)
reviewer1.rate_hw(student1, 'Git', 9)
reviewer1.rate_hw(student1, 'Python', 10)

# студенты выставляют оценки лекторам:

student1.rate_lecture(lecturer1, 'Git', 9)
student1.rate_lecture(lecturer2, 'Python', 6)
student2.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer1, 'Python', 9)

# вывод информации о студенте/лекторе/проверяющем:
print(student1)

# сравнение оценок студентов и лекторов:

print(student1 == student2)
print(lecturer1 > lecturer2)


# подсчет средней оценки всех студентов за один курс:

def students_grades(stud_list, course):
    all_grades = []
    for student in stud_list:
        if course in student.grades.keys():
            all_grades.extend(list(student.grades[course]))
    return round(sum(all_grades) / len(all_grades), 2)


print(students_grades(student_list, 'Python'))


# подсчёт средней оценки за лекции в рамках курса:

def lecturers_grades(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades.keys():
            all_grades.extend(list(lecturer.grades[course]))
    return round(sum(all_grades) / len(all_grades), 2)


print(lecturers_grades(lecturers_list, 'Python'))
