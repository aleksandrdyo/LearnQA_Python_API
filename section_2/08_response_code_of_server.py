import requests

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

#response = requests.post("https://playground.learnqa.ru/api/check_type")
#response = requests.post("https://playground.learnqa.ru/api/get_500")
#response = requests.post("https://playground.learnqa.ru/api/something")
#301 редирект постояный
#параметр allow_redirects - true(по дефолту) разрешает редирект до конечной точки или false не разрешает редирект и в ответ приходят данные только от первого запроса
response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True, headers=headers)
#302 редирект временный и может исчезнуть
#response = requests.post("https://playground.learnqa.ru/api/302")



first_response = response.history[0]
second_response = response

print(first_response.url)
print(second_response.url)

print(response)
print(response.status_code)

if response.status_code == 200:
    print("status code is 200")
elif response.status_code == 301:
    print("status code is 301")
elif response.status_code == 403:
    print("status code is 403")
else:
    print("something")

#print(response.text)