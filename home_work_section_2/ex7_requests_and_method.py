import requests

link = "https://playground.learnqa.ru/ajax/api/compare_query_type"

response_post = requests.post(link, data={"method": "POST"})
response_get = requests.get(link, params={"method": "GET"})
response_put = requests.put(link, data={"method": "PUT"})
response_delete = requests.delete(link, data={"method": ""})
response_head = requests.head(link, data={"method": "HEAD"})


print("1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.")
print(response_post.text)
print(response_get.text)
print(response_put.text)
print(response_delete.text)


print("2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.")
print(response_head.text)

print("3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.")
print(response_post.text)
print(response_get.text)
print(response_put.text)
print(response_delete.text)

print("4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.")
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’
# и так далее. И так для всех типов запроса.
# Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок.
# Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

method = ['GET', 'POST', 'PUT', 'DELETE']

for x in method:
    response_get = requests.get(link, params={f"method": x})
    print("for GET request, method is", x, "status code is", response_get.status_code, response_get.text)

for x in method:
    response_post = requests.post(link, data={f"method": x})
    print("for POST request, method is", x, "status code is", response_post.status_code, response_post.text)

for x in method:
    response_put = requests.put(link, data={f"method": x})
    print("for PUT request, method is", x, "status code is", response_put.status_code, response_put.text)

for x in method:
    response_delete = requests.delete(link, data={f"method": x})
    print("for DELETE request, method is", x, "status code is", response_delete.status_code, response_delete.text)