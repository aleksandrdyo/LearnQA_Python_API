import pytest
import requests

link = "https://playground.learnqa.ru/api/homework_header"
response = requests.get(link)

header_value = "Some secret value"
header = "x-secret-homework-header"

get_header_value = response.headers.get(header)

print(get_header_value)

assert get_header_value == header_value, "header value is not correct"

#Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py