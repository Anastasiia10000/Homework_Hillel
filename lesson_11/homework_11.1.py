# # Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
# # сторона_а (довжина сторони a).
# # кут_а (кут між сторонами a і b).
# # кут_б (суміжний з кутом кут_а).
# # Необхідно реалізувати наступні вимоги:

# # Значення сторони сторона_а повинно бути більше 0.
# # Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# # Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.

# Для встановлення значень атрибутів використовуйте метод setattr.

from math import sin, radians


class Rhombus:
    def __init__(self, a, angle_a):
        # if a <= 0 or (angle_a <= 0 or angle_a >= 180):
        #     raise ValueError("ValueError")
        # else:
        #     self.a = a
        #     self.angle_a = angle_a
        #     self.angle_b = 180 - angle_a

        self.a = None
        self.angle_a = None
        self.angle_b = None

        if a > 0 and (angle_a > 0 and angle_a) < 180:
            setattr(self, 'a', a)
            setattr(self, 'angle_a', angle_a)
            setattr(self, 'angle_b', 180 - angle_a)
        else:
            raise ValueError("ValueError!")

    def perimeter(self):
        return 4 * self.a

    def area(self):
        return (self.a ** 2) * sin(radians(self.angle_a))

    def __str__(self):
        return (
            f"Rhombus parameters:"
            f"\nside a = {self.a} cm"
            f"\nangle a = {self.angle_a}°, angle b = {self.angle_b}°"
            f"\nperimeter = {self.perimeter()} cm"
            f"\narea = {self.area():.2f} cm²"
        )

rhombus = Rhombus(8, 75)
print(rhombus)