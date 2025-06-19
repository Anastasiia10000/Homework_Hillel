#Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
#[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
#Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
#Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі),
# вам потрібно зловити вийняток і вивести “Не можу це зробити!”
#Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
#Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”

string_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def sum_numbers_from_string(s):
    try:
        parts = s.split(',')
        total = sum(int(num) for num in parts)
        return total
    except ValueError:
        return "Can't do this!"

for string in string_list:
    result = sum_numbers_from_string(string)
    print("For string", string, "the sum is:", result)