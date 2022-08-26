import requests
import pytest
from lxml import html


class TestSecretLogin:
    #Парсинг пароля
    response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")

    tree = html.fromstring(response.text)

    locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()'

    passwords = tree.xpath(locator)

    #складываем все пароли в список
    temp = []
    for password in passwords:
        password = str(password).strip()
        temp.append(password)

    #убираем дубликаты паролей из списка
    new_list = list(set(temp))

    #авторизуемся подбирая нужный пароль и получаем куку
    for passwd in new_list:

        data = {"login": "super_admin", "password": passwd}

        link = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"

        response1 = requests.post(link, data=data)

        auth_sid = response1.cookies.get("auth_cookie")

        link2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

        #получаем куку
        response2 = requests.get(
            link2,
            cookies={"auth_cookie": auth_sid}
        )

        # Если cookie неверная, то вернет фразу "You are NOT authorized".
        # Если значение cookie “правильное”, метод вернет: “You are authorized” и выводим верный пасс
        if response2.text == "You are authorized":
            print(passwd)

        #  assert response2.content == "You are authorized", "You are NOT authorized"





