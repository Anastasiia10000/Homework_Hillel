# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print("\nTask 1")
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f"{number}x{multiplier}={result}")

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
print("\nTask 2")

"""  Написати функцію, яка обчислює суму двох чисел.
"""

def summa(a, b):
    return a + b
a = 2
b = 3
result = summa (a, b)
print(f"{a} + {b} = {result}")

# task 3
print("\nTask 3")

"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average(numbers):
    return sum(numbers) / len(numbers)
lst = list(range(1, 23, 3))
average_result = average(lst)
print("Numbers:", lst)
print(f"The average value is {average_result}")

# task 4
print("\nTask 4")

"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def order_reversed (text):
    return text[::-1]
    #return ''.join(reversed(text))

#string = input("Input value:")
string = "Text with a lot of words where I need to reverse the string or find the longest word"
string_reversed = order_reversed(string)
print(f"Reversed string: {string_reversed}")

# task 5
print("\nTask 5")

"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word (text):
    words = text.split()
    return max(words, key=len)
longest = longest_word(string)
print(f"Longest word is: {longest}")

# task 6
print("\nTask 6")

"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
print("\nTask 7")

#Порахуйте периметр фігури з task 05 та виведіть його для користувача

def perimetry (storona_1 = 1, storona_2 = 2, storona_3 = 3, storona_4 = 4):
    return storona_1 + storona_2 + storona_3 + storona_4
print("Perimetry:", perimetry())

# task 8
print("\nTask 8")

# Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
# Скількі сьогодні дітей у театральному гуртку?

def children_available ():
    boys = 24
    girls = boys / 2
    sick_leave = 1
    day_off = 2
    return int(boys + girls - sick_leave - day_off)
print("Available children in theater class today: ", children_available())

# task 9
print("\nTask 9")

# Михайло разом з батьками вирішили купити комп’ютер, скориставшись послугою «Оплата частинами».
# Відомо, що сплачувати необхідно буде півтора року по 1179 грн/місяць.
# Обчисліть вартість комп’ютера.

def computer_price (credit_period, credit_per_month):
    credit_sum = credit_period * credit_per_month
    return credit_sum
print("The cost of the computer(UAH):",computer_price(credit_period = 18, credit_per_month = 1179))

# task 10
print("\nTask 10")
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
import random

def even_sum (random_list):
    even_numbers = [number for number in random_list if number % 2 == 0]
    if not even_numbers:
        print("No even sum in the list")
        return 0
    return sum(even_numbers)

random_list = random.sample(range(1, 100), 10)
print("Random list:", random_list)
print("Even sum:", even_sum(random_list))





