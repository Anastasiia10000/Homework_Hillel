# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
print("Task 01")
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n"'
    '—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
print(alice_in_wonderland)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
print("Task 02")
for character in alice_in_wonderland:
    if character =="'":
        print("Apostrophes in text:", character)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print("Task 03")
print("Full text:\n",alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
print("Task 04")
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
total_area = black_sea + azov_sea
print("Total area of azov and black sea (km2):",total_area)

# task 05
print("Task 05")
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарскладів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_storage = 375291
first_and_second_storage = 250449
second_and_third_storage = 222950
first_storage = total_storage - second_and_third_storage
third_storage = total_storage - first_and_second_storage
second_storage = total_storage - first_storage - third_storage
print("Number of goods on 1st storage:",first_storage)
print("Number of goods on 2nd storage:",second_storage)
print("Number of goods on 3rd storage:",third_storage)

# task 06
print("Task 06")
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
credit_period = 18
credit_per_month = 1179
credit_sum = credit_period * credit_per_month
print("The cost of the computer(UAH):",credit_sum)

# task 07
print("Task 07")
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("Remainder from division:")
print("a) 8019 : 8 =", 8019 % 8)
print("b) 9907 : 9 =", 9907 % 9)
print("c) 2789 : 5 =", 2789 % 5)
print("d) 7248 : 6 =", 7248 % 6)
print("e) 7128 : 5 =", 7128 % 5)
print("f) 19224 : 9 =", 19224 % 9)

# task 08
print("Task 08")
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
large_pizza = 4 * 274
middle_pizza = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
total_order_cost = large_pizza + middle_pizza + juice + cake + water
print("Total order cost (UAH):",total_order_cost)

# task 09
print("Task 09")
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photo_number = 232
one_page = 8
pages = total_photo_number // one_page
remaining_photo = total_photo_number % one_page
if remaining_photo > 0:
    pages +=1
print("Ihor needs following number of pages:", pages)

# task 10
print("Task 10")
"""
Родина зібралася в автомобільну подорож із Харкова в Будбензина-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
gas_consumption = 9
gas_tank = 48
total_gas = (distance / 100) * gas_consumption
print("Total gasoline needed for a trip (l):", total_gas)
refuel_times = total_gas // gas_tank
remaining_refuel = total_gas % gas_tank
if remaining_refuel > 0:
    refuel_times +=1
print("The minimum number of times a family needs to stop by to refuel:", refuel_times)