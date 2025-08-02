#homework_09
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
            message = f"GPA is changed from {self.grade} to {new_grade}"
            self.grade = new_grade
        else:
            message = "GPA without changes"
        return message

student1 = Student("Anastasiia", "Kalyta", 30, 90)
student2 = Student("Yurii", "Yuriyevich", 25, 90)

print("Student 1")
print(student1.greet())
print(student1.change_grade(97.5))
print(student1.greet())

print("\nStudent 2")
print(student2.greet())
print(student2.change_grade(90))
print(student2.greet())

#homework_07 > task3
def average(numbers):
    return sum(numbers) / len(numbers)
lst = list(range(1, 23, 3))
average_result = average(lst)
print("Numbers:", lst)
print(f"The average value is {average_result}")

#homework_07 > task9
# Михайло разом з батьками вирішили купити комп’ютер, скориставшись послугою «Оплата частинами».
# Відомо, що сплачувати необхідно буде півтора року по 1179 грн/місяць.
# Обчисліть вартість комп’ютера.

def computer_price (credit_period, credit_per_month):
    credit_sum = credit_period * credit_per_month
    return credit_sum
print("The cost of the computer(UAH):",computer_price(credit_period = 18, credit_per_month = 1179))