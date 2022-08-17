import requests
import pytest
import json


# class TestCheckUserAgent:
#     data1 = [
#         (
#             "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
#             "Mobile",
#             "No",
#             "Android"
#         ),
#         (
#             "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
#             "Mobile",
#             "Chrome",
#             "iOS"
#         ),
#         (
#             "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
#             "Googlebot",
#             "Unknown",
#             "Unknown"
#         ),
#         (
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
#             "Googlebot",
#             "Chrome",
#             "No"
#         ),
#         (
#             "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
#             "Mobile",
#             "No",
#             "iPhone"
#         )
#     ]

    # @pytest.mark.parametrize('agent, platform, browser, device', data)
    # def test_check_agent(self, agent, platform, browser, device):
    #     url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
    #     data = {"user-agent": agent}
    #
    #     response = requests.get(url, headers=data)
    #     obj = json.loads(response.text)
    #
    #     assert obj.get("browser") == browser
    #     assert obj.get("device") == device
    #     assert obj.get("platform") == platform

# data = {
#     'email': 'vinkotov@example.com',
#     'password': '1234'
# }
#
# response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
#
# auth_sid = response1.cookies.get("auth_sid")
# token = response1.headers.get("x-csrf-token")
# user_id_from_auth_method = response1.json()["user_id"]
# print(auth_sid)
# print(token)
# print(user_id_from_auth_method)
#
# response2 = requests.get(
#     f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method}",
#     headers={'x-csrf-token': token},
#     cookies={'auth_sid': auth_sid}
# )
#
#
# print(response2.content)

class TestParametrize:
    data = [
        {'username': 'test1',
        'lastname': 'test2'}
    ]


    @pytest.mark.parametrize('tests', data)
    def test_dict(self, tests):
        print(tests)



    # names = [
    #     ("Vitalii"),
    #     ("Arseniy"),
    #     ("")
    # ]
    #
    # @pytest.mark.parametrize('name', names)
    # def test_hello_call(self, name):
    #     data = {"name": name}
    #     print(data)


x = 5

def func():
    print(x)
    x = 3


func()