import requests

link = "https://playground.learnqa.ru/api/hello"
response = requests.get(link)

print(response.text)



