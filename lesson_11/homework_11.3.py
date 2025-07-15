# Створіть клас Employee, який має атрибути name та salary.
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників.
# Клас TeamLead повинен мати всі атрибути як Manager (ім('я, зарплата, відділ), '
# а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Employee):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size

    def __str__(self):
        return (
            f"TeamLead: {self.name}\n"
            f"Salary: {self.salary}\n"
            f"Department: {self.department}\n"
            f"Programming Language: {self.programming_language}\n"
            f"Team Size: {self.team_size}"
        )

person1 = TeamLead("Anastasiia Kalyta", 10000, "DSL", "Python", 10)
print(person1)