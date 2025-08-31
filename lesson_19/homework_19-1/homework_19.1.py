"""Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi
у виглядi JSON про фото зробленi ровером “Curiosity” на Марсi.
Серед цих даних є посилання на фото якi потрiбно розпарсити
i потiм за допомогою додаткових запитiв скачати i зберiгти цi фото
як локальнi файли mars_photo1.jpg , mars_photo2.jpg .
Завдання потрiбно зробити використовуючи модуль requests"""

import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
    photos = data['photos'] #список фото

    for i, photo in enumerate(photos, start=1): #обходимо всі фото в JSON
        url_img = photo['img_src']
        response_img = requests.get(url_img)

        if response_img.status_code == 200:
            filename = f'mars_photo{i}.jpg'
            with open(filename, 'wb') as file:
                file.write(response_img.content)
            print(f'Photo is saved as {filename}')
        else:
            print(f'Downloading is failed for photo {i}')

else:
    print('Request error. Code:', response.status_code)







