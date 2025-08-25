"""
# У venv Python встановiть Flask за допомогою команди pip install flask
# Створiть у окремiй директорiї файл app.py та скопiюйте у нього код файлу app.py
# який приведено нижче в початкових даних.
# Запустiть http сервер за допомогою команди python app.py
# Сервер стартує за базовою адресою http://127.0.0.1:8080

Враховуючи документацiю яку наведено нижче вам потрiбно написати код який використовуючи модуль request
зробить через POST upload якогось зображення на сервер,
за допомогою GET отримає посилання на цей файл
и потiм за допомогою DELETE зробить видалення файлу з сервера
"""
import requests
import os

# POST upload якогось зображення на сервер
post_url = 'http://127.0.0.1:8080/upload'
image_to_upload = "shutterstock-450886696.jpg"

with open(image_to_upload, 'rb') as image:
    files = {'image': image}
    response = requests.post(post_url, files=files) # Виконання POST-запиту з файлом

if response.status_code == 201:
    data = response.json()  # отримання даних у форматі JSON
    print('Image is uploaded:', data)

    image_url = data["image_url"]   # дістає зі словника data значення ключа "image_url" : "http://127.0.0.1:8080/uploads/example.jpg"
    filename = os.path.basename(image_url)  # -> з урла дістає тільки ім’я файлу, example.jpg
else:
    print('Error. Status code:', response.status_code)


# GET отримає посилання на цей файл
get_url = f"http://127.0.0.1:8080/image/{filename}"
headers = {"Content-Type": "text"}  # щоб сервер повернув JSON, а не саму картинку
response = requests.get(get_url, headers=headers)

if response.status_code == 200:
    print("Image info is received:", response.json())
else:
    print("Error while GET. Status code:", response.status_code, response.text)

# DELETE зробить видалення файлу з сервера
delete_url = f"http://127.0.0.1:8080/delete/{filename}"
response = requests.delete(delete_url)

if response.status_code == 200:
    print('Image is deleted successfully', response.json())
else:
    print('Error while DELETE. Status code:', response.status_code, response.text)

