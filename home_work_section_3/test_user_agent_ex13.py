import requests

link = "https://playground.learnqa.ru/ajax/api/user_agent_check"

response = requests.get(link)

print(response.text)