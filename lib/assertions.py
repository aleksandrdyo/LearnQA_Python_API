from requests import Response
import json
import json.decoder


# в этом классе лежат функции, которые расширяют проверки внутри тестов
class Assertions:
    #Убеждаемся что значение внутри json доступно по поределенному имени и равняется ожидаемому
    #Делаем метод статическим, так как класс ассершенс не является прямым наследником для наших тестов,
    #и чтоб использовать функции этого класс в тестах, нам потребуется каждый раз создавать объект ассершин
    #фызывать функции от объекта, что не совсем удобно, либо сделать функцию статичексой через Статик метод
    #На выходе функция получает, объект с ответом сервера, чтоб получить из него текст, также имя по которому
    #искать значение в json, ожидаемой значение и текст ошибки, если это значние не дуается найти
    #Функция с помошью ассерт сравнивает его с ожидаемым
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    #Метод для проверки что возвращается json формат
    #И что нужный ключ есть в json
    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"

        for name in names:
            assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"

        assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'. But it's present"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual:{response.status_code}"


