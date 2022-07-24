import requests

link = "https://playground.learnqa.ru/ajax/api/compare_query_type"

response_post = requests.post(link, data={"param1":"value1"})
response_get = requests.get(link)
response_put = requests.put(link)
response_delete = requests.delete(link)

print(response_post.status_code)
print(response_get)
print(response_put)
print(response_delete)

a = response_post.text
print(a)
#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’
# и так далее. И так для всех типов запроса. Найти такое сочетание,
# когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок.
# Или же наоборот, когда типы совпадают, но сервер считает, что это не так.