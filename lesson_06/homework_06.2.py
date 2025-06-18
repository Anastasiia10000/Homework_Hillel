# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

text = input("Please, enter a word with 'h' character: ")

while 'h' not in text and 'H' not in text:
    text = input("Not with 'h' character. Please, enter again: ")
else:
    print('Your word is correct!')

