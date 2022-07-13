import requests

link = "https://playground.learnqa.ru/api/get_text"

request = requests.get(link)

print(request.text)
