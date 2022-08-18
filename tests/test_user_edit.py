import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()

        #response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
        response1 = MyRequests.post("/user/", data=register_data)
        # print(response1.text)
        # print(response1.content)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # print(email)
        # print(first_name)
        # print(password)
        # print(user_id)

        #LOGIN
        login_data = {
            'email': email,
            'password': password,
        }

        #response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

        #GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}

        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"

        )

    def test_edit_negative(self):
        # REGISTER USER 1
        register_data = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN USER 1
        login_data = {
            'email': email,
            'password': password,
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # - Попытаемся изменить данные пользователя, будучи неавторизованными
        # FAKE EDIT NOT AUTH
        new_name = "Changed Name"
        fake_token = "123123"
        fake_auth_sid = "123123"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": fake_token},
            cookies={"auth_sid": fake_auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 400)

        # REGISTER USER 2
        register_data2 = self.prepare_registration_data()

        response4 = MyRequests.post("/user/", data=register_data2)

        Assertions.assert_code_status(response4, 200)
        Assertions.assert_json_has_key(response4, "id")

        email2 = register_data['email']
        first_name2 = register_data['firstName']
        password2 = register_data['password']
        user_id2 = self.get_json_value(response1, "id")

        # LOGIN USER 2
        login_data2 = {
            'email': email2,
            'password': password2,
        }

        response5 = MyRequests.post("/user/login", data=login_data2)

        auth_sid2 = self.get_cookie(response5, "auth_sid")
        token2 = self.get_header(response5, "x-csrf-token")

        # - Попытаемся изменить данные пользователя, будучи авторизованными другим пользователем
        # EDIT NOT AUTH
        new_name2 = "Changed Fake Name"

        response6 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token2},
            cookies={"auth_sid": auth_sid2},
            data={"firstName": new_name2}
        )
        # print(response6.status_code)
        # print(response6.content)
        Assertions.assert_code_status(response6, 400)
        # тест падает, ожидаем 400, приходит 200, и данные другого юзера меняются

        # - Попытаемся изменить email пользователя, будучи авторизованными тем же пользователем, на новый email без символа @
        new_email = "learnqatest123example.com"

        response7 = MyRequests.put(
            f"/user/{user_id2}",
            headers={"x-csrf-token": token2},
            cookies={"auth_sid": auth_sid2},
            data={"email": new_email}
        )
        # print(response7.status_code)
        # print(response7.content)
        Assertions.assert_code_status(response7, 400)

        # - Попытаемся изменить firstName пользователя, будучи авторизованными тем же пользователем, на очень короткое значение в один символ
        first_name3 = "m"

        response8 = MyRequests.put(
            f"/user/{user_id2}",
            headers={"x-csrf-token": token2},
            cookies={"auth_sid": auth_sid2},
            data={"firstName": first_name3}
        )
        # print(response8.status_code)
        # print(response8.content)
        Assertions.assert_code_status(response8, 400)
