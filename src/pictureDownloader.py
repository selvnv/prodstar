import requests
import os
import random as rnd

# Ключ, необходимый для использования Pixabay API
API_KEY = '45305139-337344c749e506a45c3dc7ffd'

# Ввод из консоли изображения, которое нужно найти
image_to_find = '+'.join(input('Enter which picture you want to find: ').split())

# Составление поискового запроса
url = f'https://pixabay.com/api/?key={API_KEY}&q={image_to_find}&image_type=all'

# Получить данные по запросу (строкового типа)
response = requests.get(url)

# Приведение ответа к формату JSON
data = response.json()

# Выбор случайного элемента (метаданных) данных ответа
random_hit = rnd.choice(data['hits'])

# Получение из метаданных изображения ссылки для скачивания
image_url = random_hit['largeImageURL']

# Получить из метаданных изображения его идентификатор
# Идентификатор станет именем сохраняемого файла
image_id = random_hit['id']

# Выполнение запроса
# Ответ - картинка в виде последовательности байт, которая сохраняется в image_data
image_data = requests.get(image_url).content

# Определение пути к папке с загруженными картинками
path_to_downloads = os.path.join(os.getcwd(), 'downloads')

# Запись байтовых данных в файл с нужным расширением
with open(os.path.join(path_to_downloads,  f'{image_id}.jpg'), mode='wb') as file:
    file.write(image_data)