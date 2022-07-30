import requests
import pytest

class TestShortPhrase:
    def test_short_phrase(self):
        phrase = input("Set a phrase, max symbol - 15: ")
        count = len(phrase)
        limit = 15


        assert count < limit, "phrase is more then 15 symbol"

#Внимание, чтобы pytest не игнорировал команду ввода с клавиатуры, запускать тест нужно с ключиком "-s": python -m pytest -s my_test.py

