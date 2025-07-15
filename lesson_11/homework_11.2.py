# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"Perimeter is {self.perimeter()}. Area is {self.area()}."

class Square(Figure):

    def __init__(self, side):
        self.__side = side

    def perimeter(self):
        return 4 * self.__side

    def area(self):
        return self.__side ** 2

    def __str__(self):
        return "This is Square >> " + super().__str__()


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def perimeter(self):
        return 2 * pi * self.__radius

    def area(self):
        return pi * (self.__radius)**2

    def __str__(self):
        return "This is Circle >> " + super().__str__()

class Rectangular(Figure):
    def __init__(self, side1, side2):
        self.__side1 = side1
        self.__side2 = side2

    def perimeter(self):
        return 2 * self.__side1 + 2 * self.__side2

    def area(self):
        return self.__side1 * self.__side2

    def __str__(self):
        return "This is Rectangular >> " + super().__str__()

class Parallelogram(Figure):
    def __init__(self, side1, side2, height1):
        self.__side1 = side1
        self.__side2 = side2
        self.__height1 = height1

    def perimeter(self):
        return 2 * (self.__side1 + self.__side2)

    def area(self):
        return self.__side1 * self.__height1

    def __str__(self):
        return "This is Parallelogram >> " + super().__str__()

figures = [Circle(3), Square(4), Rectangular(3, 4), Parallelogram(3, 5, 4)]

for figure in figures:
    print(figure)
