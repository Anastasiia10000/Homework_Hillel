# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючий студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, name, surname, age, grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.grade = grade

    def greet(self):
        return f"My full name is {self.name} {self.surname}. I'm {self.age} years old. My GPA is {self.grade}"

#    def change_grade(self, new_grade):
#        self.grade = new_grade
#        return f"The grade is changed"

    def change_grade(self, new_grade):
        if new_grade != self.grade:
            print(f"GPA is changed from {self.grade} to {new_grade}")
            self.grade = new_grade
        else:
            print("GPA without changes")



student1 = Student("Anastasiia", "Kalyta", 30, 90)
student2 = Student("Yurii", "Yuriyevich", 25, 90)

print("Student 1")
print(student1.greet())
student1.change_grade(97.5)
print(student1.greet())

print("\nStudent 2")
print(student2.greet())
student2.change_grade(90)
print(student2.greet())