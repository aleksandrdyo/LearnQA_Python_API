import pytest
import requests
from lib.base_case import BaseCase

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

        response1 = requests.post(link, data=data)
        print(response1)
        # после логина и пароля, получем авторизационные куки "auth_sid" с уникальным значением,
        # которые в дальнейшим используются ко всем запросом от данного юзера будут прикладываться данные куки, чтобы сервер понимал, что запросы идут от нашего юзера
        assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
        # второй заголовок токент x-csrf-token уникальным значением, используется для безопасности, не ползволяет потделовать куки от данного юзера
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response"
        # только при олучение авторизационные куки и заголовока, последующие запросы будут считаться авторизованными
        assert "user_id" in response1.json(), "There is no user id in the response"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id_from_auth_method = response1.json()["user_id"]

        self.link2 = "https://playground.learnqa.ru/api/user/auth"


    def test_auth_user(self):

        response2 = requests.get(
            self.link2,
            headers={"x-csrf-token":self.token},
            cookies={"auth_sid":self.auth_sid}
        )

        assert "user_id" in response2.json(), "There is no user id in the response"
        user_id_from_check_method = response2.json()["user_id"]

        assert self.user_id_from_auth_method == user_id_from_check_method , "User id from auth method is not equal to user id from check method"




    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_check(self, condition):

        if condition == "no_cookie":
            response2 = requests.get(self.link2, headers={"x-csrf-token": self.token})
        else:
            response2 = requests.get(self.link2, headers={"auth_sid": self.auth_sid})

        assert "user_id" in response2.json(), "There is no user id in the second response"

        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_check_method == 0, f"User is authorized with condition {condition}"

