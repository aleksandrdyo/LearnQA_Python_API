import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import pytest
from datetime import datetime
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):

    #link = "https://playground.learnqa.ru/api/user/"

    # def setup(self):
    #     base_part = "learnqa"
    #     domain = "example.com"
    #     random_part = datetime.now().strftime("%m%d%Y%H%M%S")
    #     self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        # data = {
        #     'password': '123',
        #     'username': 'learnqa',
        #     'firstName': 'learnqa',
        #     'lastName': 'learnqa',
        #     'email': self.email
        # }

        #response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 200)
        #assert response.status_code == 200, f"Unexpected status code {response.status_code}"
        #print(response.content)
        #print(response.text)
        #print(response.status_code)
        Assertions.assert_json_has_key(response, "id")

    #@pytest.mark.parametrize("testdata", data)
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        # data = {
        #     'password': '123',
        #     'username': 'learnqa',
        #     'firstName': 'learnqa',
        #     'lastName': 'learnqa',
        #     'email': email
        # }

        #print(testdata)

        # response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        response = MyRequests.post("/user/", data=data)

        #print(response)
        #print(response.status_code)
        #print(response.content)

        Assertions.assert_code_status(response, 400)
        # assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"

#- Создание пользователя с некорректным email - без символа @
    def test_create_user_without_et(self):

        email = 'vinkotov2example.com'

        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        # response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        response = MyRequests.post("/user/", data=data)

        assert "@" not in email, "email with et symbol"
        Assertions.assert_code_status(response, 400)
        #assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode(
            "utf-8") == "Invalid email format"

#- Создание пользователя с очень коротким именем в один символ
    def test_update_conference_session_field_name_len(self):

        name_len = 1
        email = ""

        for i in range(0, name_len):
            email += "a"

        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
        # response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        #assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode(
            "utf-8") == "The value of 'email' field is too short"

#- Создание пользователя с очень длинным именем - длиннее 250 символов
    def test_create_user_with_long_email(self):

        email = ""
        name_len = 251

        for i in range(0, name_len):
            email += "a"

        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        # response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        response = MyRequests.post("/user/", data=data)

        #print(response.content.decode("utf-8"))

        Assertions.assert_code_status(response, 400)
        #assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode(
            "utf-8") == "The value of 'email' field is too long"

# - Создание пользователя без указания одного из полей -
# с помощью @parametrize необходимо проверить,
# что отсутствие любого параметра не дает зарегистрировать пользователя
    data1 = [
        {
            'password': '12345678',
            #'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
           'email': 'vinkotov111@example.com'
         }
    ]

    @pytest.mark.parametrize('datas', data1)
    def test_create_user_without_filed(self, datas):

        response = requests.post("https://playground.learnqa.ru/api/user/", data=datas)

        assert response.status_code == 400, response.content
        #assert response.content.decode("utf-8") == response.content




