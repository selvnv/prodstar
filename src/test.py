import requests

response = requests.get('https://ya.ru')

print(response.status_code)
print(response.content)