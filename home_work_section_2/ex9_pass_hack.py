import requests

link = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
link1 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
link2 = "https://en.wikipedia.org/wiki/List_of_the_most_common_passwords"


response = requests.post(link, data={"login":"super_admin", "password":""})
response1 = requests.post(link1, data={"cookiex`":""})
print(response.text)
print(response1.text)
response2 = requests.post(link2)
print(response2.text)
