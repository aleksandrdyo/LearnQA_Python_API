import pytest
import requests

class TestFirstApi:

    names = [
        ("Vitalii"),
        ("Arseniy"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {"name": name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is n field 'answer' in the response"

        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"

        #expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "actual text in the response is not correct"
