"""
1. Створення моделі даних:
Створіть просту модель даних для системи управління студентами.Модель може містити таблиці для студентів, курсів та їх відношень.
Кожен студент може бути зареєстрований на декілька курсів. Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.

2. Виконання базових операцій:
Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу.
Переконайтеся, що ці зміни коректно відображаються у базі даних.

3. Запити до бази даних:
Напишіть запити до бази даних, які повертають інформацію про студентів, зареєстрованих на певний курс, або курси, на які зареєстрований певний студент.

4. Оновлення та видалення даних:
Реалізуйте можливість оновлення даних про студентів або курси, а також видалення студентів з бази даних.

5. Можна використовувати будь яку ORM на Ваш вибір """

from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey, inspect
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base() #функція з SQLAlchemy, яка створює "базовий клас" для таблиць

# 1. Моделі
# Таблиця зв'язку many-to-many
student_courses = Table(
    'student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base): # Модель "Student"
    __tablename__ = 'students' # буде створена таблиця "students"
    id = Column(Integer, primary_key=True)    # Первинний ключ (PRIMARY KEY)
    name = Column(String)

    courses = relationship('Course', secondary=student_courses, back_populates='students') # зв’язок many-to-many через таблицю student_courses

# courses — це не колонка в БД, а "псевдополе" (існує лише у Python-коді), яке при завантаженні покаже всі курси студента.
# relationship("Course") каже: ця модель пов’язана з класом Course.
# back_populates="student" означає, що у класі Course ми теж оголосимо зв’язок у зворотний бік.

class Course(Base): # Модель "Course"
    __tablename__ = 'courses' # буде створена таблиця "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)

    students = relationship('Student', secondary=student_courses, back_populates='courses') # Зворотній зв’язок до Student
    # ForeignKey вказує, що це зовнішній ключ (зв'язок із таблицею students)


# 2. Підключення до БД і створення таблиць

# створюємо файл [name].db у поточній директорії за допомогою драйвера SQLite
# echo=True дозволяє бачити SQL-запити в консолі (для дебагу)
engine = create_engine("sqlite:///homework_22.db", echo=False)
Base.metadata.create_all(engine) # Створюємо всі таблиці, які визначені через Base (Student і Course)

Session = sessionmaker(bind=engine) # Створення сесії для роботи з БД, Session = об’єкт, через який робимо всі операції з БД
session = Session()

# 3. Операції CRUD
# ---------- CREATE ----------
# CREATE - 5 курсів, якщо їх ще нема
course_titles = ["Mathematics", "Physics", "Programming", "History", "English"]
existing_courses = {c.title for c in session.query(Course).all()}

for title in course_titles:
    if title not in existing_courses:
        session.add(Course(title=title))
session.commit()

courses = session.query(Course).all()  # Оновлений список курсів

# CREATE - 20 студентів, якщо їх ще нема
students_courses = {
    "Helen Jackson": ["Mathematics", "Programming"],
    "Maria Martin": ["Physics", "English"],
    "Oleg Smith": ["History", "Mathematics", "English"],
    "John Lewis": ["Programming"],
    "Peter Jackson": ["Mathematics", "History"],
    "Victoria Brown": ["Programming", "English"],
    "Anna Thompson": ["Physics", "Mathematics"],
    "Alexander Walker": ["History", "English"],
    "Dmitry Taylor": ["Programming", "Mathematics"],
    "Arthur Robinson": ["History", "English"],
    "Julia Anderson": ["Mathematics", "Physics"],
    "Tanya White": ["Programming"],
    "George Garcia": ["History", "English"],
    "Natalie Lee": ["English", "Physics"],
    "Sergey Clark": ["Programming", "Mathematics"],
    "Kate Rodriguez": ["History", "English"],
    "Michael Martinez": ["Mathematics", "Programming"],
    "Irene Harris": ["Physics"],
    "Andrew Hall": ["Mathematics", "English", "Physics"],
    "Svetlana Johnson": ["Programming", "History"]
}

existing_students = {s.name for s in session.query(Student).all()}

for name, course_list in students_courses.items():
    if name not in existing_students:
        student = Student(name=name)
        student.courses = [c for c in courses if c.title in course_list]
        session.add(student)

session.commit()

# CREATE — додаємо нового студента
new_student = Student(name="Ivan Petrov")
new_student.courses = [c for c in courses if c.title in ["Mathematics", "English"]]
session.add(new_student)
session.commit()
print("New student is added:", new_student.name)


# READ — всі студенти з їх курсами
for s in session.query(Student).all():
    print(f"ID {s.id} | {s.name}: {[c.title for c in s.courses]}")


# READ — студенти на певному курсі
course = session.query(Course).filter_by(title="Programming").first()
if course:
    print("Students on 'Programming' course:", [s.name for s in course.students])


# READ — курси конкретного студента
student = session.query(Student).filter_by(name="Oleg Smith").first()
if student:
    print("Oleg Smith courses:", [c.title for c in student.courses])


# UPDATE — змінюємо ім'я студента
student_to_update = session.query(Student).filter_by(name="Ivan Petrov").first()
if student_to_update:
    old_name = student_to_update.name
    student_to_update.name = "Ivan Petrenko"
    session.commit()
    print(f"Student name is updated: {old_name} → {student_to_update.name}")


# DELETE — видаляємо студента
students_to_delete = session.query(Student).filter_by(name="Ivan Petrenko").all()
if students_to_delete:
    for s in students_to_delete:
        session.delete(s)
    session.commit()
    print(f"{len(students_to_delete)} student(s) with name '{students_to_delete[0].name}' deleted")
else:
    print("No students with that name found")