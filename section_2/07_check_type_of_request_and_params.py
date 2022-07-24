import requests

#только для get запроса параметры передаются через params, для остальных запросов, передаются через data
response1 = requests.get('https://playground.learnqa.ru/api/check_type', params={"param1":"value1"})
response2 = requests.post('https://playground.learnqa.ru/api/check_type', data={"param1":"value1"})
response3 = requests.delete('https://playground.learnqa.ru/api/check_type', data={"param1":"value1"})
response4 = requests.put('https://playground.learnqa.ru/api/check_type', params={"param1":"value1"})

print(response3)
print(response3.text)
