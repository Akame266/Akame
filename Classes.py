class Student:
    def __init__(self, name=None, surname=None, *grades):
        self.__name = name
        self.__surname = surname
        self.__grades = list(grades)

    def display_name(self):
        a = str(self.__name) + ' ' + str(self.__surname)
        return a

    def add_grades(self, *args):
        if self.__grades:
            self.__grades = self.__grades + list(args)
        else:
            self.__grades = args

    def show_grades(self):
        a = str(self.__name) + ' ' + str(self.__surname)
        if self.__grades:
            return f'Оценки, которые получил студент {a} : {list(self.__grades)}'
        else:
            return f'Студент {a} еще не получил оценок'

    def change_grades(self, *new_grades):
        self.__grades = new_grades

    def change_name(self, new_name=None):
        self.__name = new_name

    def change_surname(self, new_surname=None):
        self.__surname = new_surname


class Group:
    def __init__(self, group_name=None, *students):
        self.group_name = group_name
        self.students = list(students)

    def add_student(self, *students):
        for i in students:
            self.students.append(i)

    def show_group(self):
        a = []
        if self.students:
            for i in self.students:
                a.append(i.display_name())
            return f'Название группы: "{self.group_name}", список студентов группы: {a}'
        else:
            return f'В группе "{self.group_name}" еще нет студентов.'


s = Student('Вася', 'Уткин', 1)
s1 = Student('Петя', 'Мансуров')
s2 = Student('Кира', 'Найтли', 1, 55, 1, 35, 1)
s3 = Student('Ирина', 'Полон', 1, 2, 4)
g = Group('Дрим Тим', s, s1)
print(g.show_group())
g.add_student(s2, s3)
print(g.show_group())
print(s1.show_grades())
s1.add_grades(1,2,2,2)
print(s1.show_grades())
s1.change_grades(1,1,1,1)
print(s1.show_grades())
print(s.show_grades())

