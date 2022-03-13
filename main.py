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

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.gradebook:
                lecturer.gradebook[course] += [grade]
            else:
                lecturer.gradebook[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        summ = 0
        if len(self.grades) > 0:
            for key, value in self.grades.items():
                summ = summ + sum(value)/len(value)
            return summ/len(self.grades)
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        text = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.average_grade():.1f} \nКурсы в процессе изучения: {','.join(self.courses_in_progress)} \nЗавершенные курсы: {','.join(self.finished_courses)}"
        return text

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.gradebook = {}

    def average_gradebook(self):
        summ = 0
        if len(self.gradebook) > 0:
            for key, value in self.gradebook.items():
                summ = summ + sum(value) / len(value)
            return summ / len(self.gradebook)
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.average_gradebook() < other.average_gradebook()

    def __str__(self):
        text = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_gradebook()}"
        return text

class Reviewer(Mentor):
    # def __init__(self, name, surname):
    #     super().__init__(name, surname)
    #     self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f"Имя: {self.name}  \nФамилия: {self.surname}"
        return text



student1 = Student('Ruoy', 'Eman', 'man')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['CSS']

student1.add_courses('C++')

student2 = Student('Egor', 'kalinin', 'man')

student2.courses_in_progress += ['Java']
student2.courses_in_progress += ['C++']

student2.add_courses('CSS')

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['CSS']
reviewer1.courses_attached += ['Java']

reviewer2 = Reviewer('Anna', 'Karenina')
reviewer2.courses_attached += ['Java']
reviewer2.courses_attached += ['CSS']
reviewer2.courses_attached += ['C++']


reviewer1.rate_hw(student1,'CSS', 10)
reviewer1.rate_hw(student1,'CSS', 8)
reviewer1.rate_hw(student1,'CSS', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 7)

reviewer2.rate_hw(student2,'C++', 7)
reviewer2.rate_hw(student2,'C++', 4)
reviewer2.rate_hw(student2,'C++', 2)
reviewer2.rate_hw(student2, 'Java', 7)
reviewer2.rate_hw(student2, 'Java', 8)
reviewer2.rate_hw(student2, 'Java', 4)


lecturer1 = Lecturer('Alex', 'Ivon')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['CSS']
lecturer1.courses_attached += ['Java']

lecturer2 = Lecturer('Ivan', 'Svoboda')
lecturer2.courses_attached += ['Java']
lecturer2.courses_attached += ['CSS']
lecturer2.courses_attached += ['C++']

student1.rate_lecturer(lecturer1,'CSS', 1)
student1.rate_lecturer(lecturer1,'Python', 10)

student2.rate_lecturer(lecturer2,'C++', 7)
student2.rate_lecturer(lecturer2,'Java', 9)

print(student1.grades)
print("Первый Ревьювер ")
print(reviewer1)
print("Второй Ревьювер ")
print(reviewer2)

print("__________________________________________")
print("Первый лектор ")
print(lecturer1)
print("Второй лектор ")
print(lecturer2)

print("__________________________________________")
print("Первый студент ")
print(student1)
print("Второй студент ")
print(student2)

print(student1 > student2)
print(lecturer1 > lecturer2)

def average_hw_allstudent(students,course):
    summ = 0
    for student in students:
        for key, value in student.grades.items():
            if key == course:
                summ = summ + sum(value) / len(value)
    return summ / len(students)

def average_course_alllect(lecturers,course):
    summ = 0
    for lecrurer in lecturers:
        for key, value in lecrurer.gradebook.items():
            if key == course:
                summ = summ + sum(value) / len(value)
    return summ / len(lecturers)

students_list = (student1, student2)
print(average_hw_allstudent(students_list,'Python'))

lecturer_list = (lecturer1, lecturer2)
print(average_course_alllect(lecturer_list,'Python'))