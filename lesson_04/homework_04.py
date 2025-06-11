import re

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

print("Task 01:")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
print("Task 02:")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("Task 03:")
adwentures_of_tom_sawer = re.sub(r'\s+', ' ', adwentures_of_tom_sawer).strip()
print(adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("Task 04:")
count_h = adwentures_of_tom_sawer.count("h")
print("Count of h characters -", count_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("Task 05:")
adwentures_of_tom_sawer_words = adwentures_of_tom_sawer.split()
count_capitalized = 0
for word in adwentures_of_tom_sawer_words:
    if word[0].isupper():
        count_capitalized += 1
print("Count of capitalized words -", count_capitalized)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("Task 06:")
first_index = adwentures_of_tom_sawer.find("Tom")
second_index = adwentures_of_tom_sawer.find("Tom", first_index + 1)
print("2nd position of Tom -", second_index)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("Task 07:")
adwentures_of_tom_sawer_sentences = re.split(r'(?<=[.!?]) +', adwentures_of_tom_sawer)
print("Sentences separating:\n", adwentures_of_tom_sawer_sentences)

print("Sentences iteration (additional task):")
for sentence in adwentures_of_tom_sawer_sentences:
    print(sentence)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("Task 08:")
if len(adwentures_of_tom_sawer_sentences) >= 4:
    fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
    print("4th sentense (changed to lowercase):\n", fourth_sentence)
else:
    print("Less than 4 sentenses")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("Task 09:")
starts_with_by_the_time = any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)
print("Availability of sentenses that starts with 'By the time':", starts_with_by_the_time)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("Task 10:")
last_sentence = adwentures_of_tom_sawer_sentences[-1]
word_count_last = len(last_sentence.split())
print("Count of words in last sentense:", word_count_last)
