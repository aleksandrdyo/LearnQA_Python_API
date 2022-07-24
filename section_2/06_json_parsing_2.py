from json.decoder import JSONDecodeError
import requests

response = requests.get('https://playground.learnqa.ru/api/get_text')
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print('Response is not a JSON format')
#парсим json, также проверяем? если в ответе нет json формата то ловим это ошибку через JSONDecodeError