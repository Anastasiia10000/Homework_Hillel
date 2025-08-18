import random


print("\n=== Generators ===")

""" Напишіть генератор, який повертає послідовність парних чисел від 0 до N."""
print("\nTask 1.1: Even number generator from 0 to N")
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

print(list(even_numbers(20)))

""" Створіть генератор, який генерує послідовність Фібоначчі до певного числа N. """
print("\nTask 1.2: Fibonacci number generator up to N")
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

print(list(fibonacci(50)))

print("\n=== Iterators ===")
"""Реалізуйте ітератор для зворотного виведення елементів списку."""
print("\nTask 2.1: Iterator to reverse the list elements.")

def random_six_numbers():
    for _ in range(6):
        yield random.randint(1, 50)

random_numbers = list(random_six_numbers())
print("List of elements:", random_numbers)

def reverse_iterator(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]

print("Reversed list:")
iterator = reverse_iterator(random_numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("Iterator is finished")


"""Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N."""
print("\nTask 2.2: Iterator to return all even numbers in the range 0 to N = 8.")
def even_iterator(n):
    for i in range(0, n + 1, 2):
        yield i

iterator = even_iterator(8)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("Iterator is finished")


print("\n=== Decorators ===")

"""Напишіть декоратор, який логує аргументи та результати викликаної функції."""
print("\nTask 3.1: Decorator for logging arguments and results")

def log_args_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Result: {result}")
        return result
    return wrapper

@log_args_and_result
def add(a, b):
    return a + b

print("Calling add(3, 5):")
add(3, 5)

"""Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції."""
print("\nTask 3.2: Decorator for catching and handling exceptions")
def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] An error occurred in {func.__name__}: {e}")
            return None
    return wrapper

@catch_exceptions
def divide(a, b):
    return a / b

print("Calling divide: 10 / 2 =", divide(10, 2))
print("Calling divide: 10 / 0 =", divide(10, 0))