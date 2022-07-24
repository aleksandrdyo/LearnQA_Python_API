import requests

link = "https://playground.learnqa.ru/api/hello"
payload = {"name":"user111"}

response = requests.get(link, params = payload)

print(response.text)
