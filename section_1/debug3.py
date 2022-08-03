import requests
import pytest

ex_val = (
    {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
    {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
    {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
    {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
    {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
)

user_agent = [
'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
]

link = "https://playground.learnqa.ru/ajax/api/user_agent_check"

for x in user_agent:
    response = requests.get(link, headers={"User-Agent": x})
    parsing_json = response.json()
    print(parsing_json)
    # print(parsing_json["platform"])
    # print(parsing_json["browser"])
    # print(parsing_json["device"])

@pytest.mark.parametrize('name', user_agent)
    def test_send_user_agent(self, name):
        response = requests.get(link, headers={"User-Agent": name})
        parsing_json = response.json()
        print(parsing_json)