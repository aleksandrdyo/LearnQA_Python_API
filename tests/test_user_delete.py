import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserDelete(BaseCase):
    def test_edit_just_created_user(self):
        #LOGIN
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")

        #Удалить пользователя по ID 2 и убедиться, что система не даст вам удалить этого пользователя.
        #DELETE NEGATIVE
        response2 = MyRequests.delete(
            f"/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
         )

        Assertions.assert_code_status(response2, 400)

        #Создать пользователя, авторизоваться из-под него, удалить, затем попробовать получить его данные по ID и убедиться, что пользователь действительно удален.
        #DELETE POSITIVE
        register_data = self.prepare_registration_data()
        response3 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response3, 200)
        Assertions.assert_json_has_key(response3, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response3, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password,
        }

        response4 = MyRequests.post("/user/login", data=login_data)

        auth_sid2 = self.get_cookie(response4, "auth_sid")
        token2 = self.get_header(response4, "x-csrf-token")

        # GET
        response5 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token2},
            cookies={"auth_sid": auth_sid2}

        )

        Assertions.assert_code_status(response5, 200)

        # DELETE
        response6 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token2},
            cookies={"auth_sid": auth_sid2},
        )

        Assertions.assert_code_status(response6, 200)

        # GET
        response7 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token2},
            cookies={"auth_sid": auth_sid2}

        )

        Assertions.assert_code_status(response7, 404)

