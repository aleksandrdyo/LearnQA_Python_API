import requests

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)

#first_response = response4.history[0]
#second_response = response4

#print(first_response.url)
#print(second_response.url)

#print(response4)
print(response.status_code)
#print(response4.text)