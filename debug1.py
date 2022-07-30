import requests

link = "https://playground.learnqa.ru/api/homework_cookie"

response = requests.get(link)
response_cookie = response.cookies.get("HomeWork")
print(response_cookie)
cookie_value = "hw_value"
assert response_cookie == "hw_value", "cookie value is not correct"


#Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py