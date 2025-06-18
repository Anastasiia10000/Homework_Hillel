# Given list of tuples (name, surname, age, profession, City location)

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
# 1 - Add your new record on the beginning of the given list
print ("Task 1: add new record on the beginning of the given list")
new_record = ('Anastasiia', 'Kalyta', 30, 'QA engineer', 'Zhytomyr')
people_records.insert(0, new_record)
for person in people_records:
    print(person)

# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
print ("\nTask 2: swap elements with indexes 1 and 5 (1<->5)")
people_records[1], people_records[5] = people_records[5], people_records[1]
for person in people_records:
    print(person)

# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result
print ("\nTask 3: all people with records indexes 6, 10, 13 have age >=30")
indexes = [6, 10, 13]

if all(i < len(people_records) for i in indexes):
    all_30_or_more = True
    for i in indexes:
        age = people_records[i][2]
        if age >= 30:
            print(f"Index {i}: 30+ years old")
        else:
            print(f"Index {i}: less than 30 years old")
            all_30_or_more = False
    print("Усі віком >= 30:", all_30_or_more)
else:
    print("List is too short to check all requested indexes.")