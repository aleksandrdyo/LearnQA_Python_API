import requests
import pytest
from lxml import html


class TestSecretLogin:
#Парсинг пароля
    response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")

    tree = html.fromstring(response.text)

    locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()'

    passwords = tree.xpath(locator)

    temp = []

    for password in passwords:
        password = str(password).strip()
        temp.append(password)

    new_list = list(set(temp))


#for x in new_list:
#    print()
    @pytest.mark.parametrize("pass", new_list)
    def get_secret_password_homework(self, passwd):
        data = {"login": "super_admin", "password": passwd}
        link = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"

        response1 = requests.post(link, data=data)

        print(response1.content)
        print(response1.status_code)

        assert response1.status_code == 200, "wrong response code"

        link2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

#

#check_auth_cookie.