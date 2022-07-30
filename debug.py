import requests

link = "https://playground.learnqa.ru/api/user/login"
data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
response1 = requests.post(link, data=data)
print(response1.text)
print(response1.cookies)
assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
print(response1.headers)
assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response"
print(response1.json())
assert "user_id" in response1.json(), "There is no user id in the response"

auth_sid = response1.cookies.get("auth_sid")
print(auth_sid)
token = response1.headers.get("x-csrf-token")
print(token)
user_id_from_auth_method = response1.json()["user_id"]
print(user_id_from_auth_method)

link2 = "https://playground.learnqa.ru/api/user/auth"
response2 = requests.get(
    link2,
    headers={"x-csrf-token":token},
    cookies={"auth_sid":auth_sid}
)
print(response2.json())

assert "user_id" in response2.json(), "There is no user id in the response"
user_id_from_check_method = response2.json()["user_id"]
print(user_id_from_check_method)
print(user_id_from_auth_method)
assert user_id_from_auth_method == user_id_from_check_method, "User id from auth method is not equal to user id from check method"


