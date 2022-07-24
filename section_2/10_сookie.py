#куки это спец файлы, которые создает клиент(браузер или дргуой моб клиент) на основе отвеа сервера,
# эти файлы имеют срок годности, которые автоматически удаляются клиентом
# у каждого куки имеются имя, значени и принадлежность к домену

import requests

payload = {"login":"secret_login", "password":"secret_pass"}

response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

print(response.text)
print(response.status_code)
print(dict(response.cookies))
print(response.headers)

