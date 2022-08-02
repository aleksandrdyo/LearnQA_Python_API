import requests

resposnse = requests.get("https://playground.learnqa.ru/api/check_type", data={"param1":"value1"})
print(resposnse.text)

#params для get запроса
#data для post запроса