# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

text = input("Please, enter your string: ")
text = text.replace(" ", "")  # delete all spaces
unique_chars = set(text) #set automatically left only unique chars
print(unique_chars)
print(len((unique_chars)))

print("Case1: with conditions/statements")
if len(unique_chars) > 10:
    print(f"{True} as {len(unique_chars)} more than 10")
else:
    print(f"{False} as {len(unique_chars)} is equal/less than 10")

print("\nCase2: simple variant")
print(len(unique_chars) > 10)
