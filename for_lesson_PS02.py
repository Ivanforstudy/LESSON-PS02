from http.client import responses


import requests
import pprint
#response = requests.get('https://www.google.com')
# print(response.status_code)
# print(response.ok)
#
# if response.ok:
#     print('Запрос успешно выполнен')
# else:
#     print('Произошла ошибка')
# response = requests.get('https://api.github.com')
# print(response.text)
# response_json = response.json()
# pprint.pprint(response_json)
# params = {
# 'q': 'JawaScript'
# }
# response = requests.get('https://api.github.com/search/repositories', params=params)
# response_json = response.json()
# pprint.pprint(response_json)
# print(f"Количество репозиториев с использованием js: {response_json['total_count']}")


# !response = requests.get('https://google.com')
# print(response.status_code)  # Вывод статус-кода
#
# print(response.headers)  # Вывод заголовка
#
# print(response.text)  # Вывод основного текста (тела)

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "тестовый post запрос",
    "body": "тестовый контент post запроса",
    "userId": 2
}
response = requests.post(url, data=data)
print(response.status_code)
print(f"Ответ - {response.json()}")




