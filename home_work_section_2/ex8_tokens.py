import requests
import json
import time

link = "https://playground.learnqa.ru/ajax/api/longtime_job"

#1) создавал задачу
#отправляем запрос, парсим json, получем токен и время
response = requests.get(link)
parsing_json = json.loads(response.text)
parsing_token = parsing_json["token"]
parsing_time = parsing_json["seconds"]

#2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
#отправляем запрос с токеном или не верным токеном и делаем проверку на верный статус или ошибку
response_token = requests.get(link, params={"token": parsing_token})
#response_token = requests.get(link, params={"token": "fake_token"})
get_status = response_token.text
parsing_status = json.loads(get_status)
#получаем список ключей из словаря list(dict) или list(dict.keys())
key = list(parsing_status.keys())
status_job = parsing_status[key[0]]

if status_job == "Job is NOT ready":
    #3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
    time.sleep(parsing_time+2)

    #4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result
    response_token1 = requests.get(link, params={"token": parsing_token})
    get_status1 = response_token1.text
    parsing_status_job = json.loads(get_status1)
    result = int(parsing_status_job["result"])
    status_job1 = parsing_status_job["status"]
    if status_job1 == "Job is ready" and result is not None:
        print(status_job1, "result is", result)
else:
    print("No job linked to this token")