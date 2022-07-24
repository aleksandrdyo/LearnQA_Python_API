import requests

link = "https://playground.learnqa.ru/api/long_redirect"

headers = {
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

response = requests.get(link, allow_redirects=True, headers=headers)

#Определяем кол-во редиректов
redirect_count = len(response.history)

#Через цыкл выводим промежуточные точки
for x in range(redirect_count):
    #print(response.history[x])
    print(response.history[x].url)

#кол-во редиректов
print("кол-во редиректов -", redirect_count)

#Итоговый url
print("итоговый URL -", response.url)
