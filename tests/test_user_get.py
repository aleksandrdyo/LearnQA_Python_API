import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserGet(BaseCase):
    def test_get_user_details_not_auth(self):
        #response = requests.get("https://playground.learnqa.ru/api/user/2")
        response = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        #response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")
        # print(auth_sid)
        # print(token)
        # print(user_id_from_auth_method)

        # response2 = requests.get(
        #     f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method}",
        #     headers={"x-csrf-token": token},
        #     cookies={"auth_sid": auth_sid}
        # )
        response2 = MyRequests.get(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        #response_as_dict = response2.json()
        #print(response_as_dict)
        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

        # Assertions.assert_json_has_key(response2, "username")
        # Assertions.assert_json_has_key(response2, "email")
        # Assertions.assert_json_has_key(response2, "firstName")
        # Assertions.assert_json_has_key(response2, "lastName")

#В этой задаче нужно написать тест, который авторизовывается одним пользователем,
# но получает данные другого (т.е. с другим ID).
# И убедиться, что в этом случае запрос также получает только username,
# так как мы не должны видеть остальные данные чужого пользователя.
    def test_get_user_details_auth_with_fake_id(self):
        register_data = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=register_data)

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        data = {
            'email': email,
            'password': password,
        }


        response2 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response2, "user_id")
        fake_user_id = 2

        response2 = MyRequests.get(
            f"/user/{fake_user_id}",
#            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        expected_fields = ["username"]
        #print(expected_fields)
        #print(response2.content)
        Assertions.assert_json_has_keys(response2, expected_fields)
