# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
import random

random_list = random.sample(range(1, 100), 10)
print(random_list)
even_sum = sum(number for number in random_list if number % 2 == 0)
print("Even sum:", even_sum)