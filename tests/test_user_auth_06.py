import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure

@allure.epic("Authorization cases")
class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookies"),
        ("no_token")
    ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        # апи методы https://playground.learnqa.ru/api/map
        link = "https://playground.learnqa.ru/api/user/login"

        response1 = MyRequests.post("/user/login", data=data)
        #response1 = requests.post(link, data=data)
        #print(response1)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

        self.link2 = "https://playground.learnqa.ru/api/user/auth"


    @allure.title("тест авторизация")
    @allure.description("This test successfully authorize user by email and password")
    def test_auth_user(self):

        # response2 = requests.get(
        #     self.link2,
        #     headers={"x-csrf-token":self.token},
        #     cookies={"auth_sid":self.auth_sid}
        # )
        response2 = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method"
        )

        # assert "user_id" in response2.json(), "There is no user id in the response"
        # user_id_from_check_method = response2.json()["user_id"]
        #
        # assert self.user_id_from_auth_method == user_id_from_check_method, "User id from auth method is not equal to user id from check method"

    @allure.title("тест авторизация")
    @allure.description("This test checks authorization status w/o sending auth cookie or token")
    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_check(self, condition):

        if condition == "no_cookie":
            #response2 = requests.get(self.link2, headers={"x-csrf-token": self.token})
            response2 = MyRequests.get(
                "/user/auth",
                headers={"x-csrf-token": self.token}
            )
        else:
            #response2 = requests.get(self.link2, headers={"auth_sid": self.auth_sid})
            response2 = MyRequests.get(
                "/user/auth",
                headers={"auth_sid": self.auth_sid}
            )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            0,
            f"User is authorized with condition {condition}"
        )

        # assert "user_id" in response2.json(), "There is no user id in the second response"
        #
        # user_id_from_check_method = response2.json()["user_id"]
        #
        # assert user_id_from_check_method == 0, f"User is authorized with condition {condition}"

