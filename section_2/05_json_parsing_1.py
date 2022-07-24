import json

string_as_json_format = '{"answer":"Hello, world"}'

#с помощью либы json парсим строки string_as_json_format- превращается в объект похожий на словать в питоне
obj = json.loads(string_as_json_format)

print(string_as_json_format)
print(obj)
key = "answer1"
#print(obj[key])

if key in obj:
    print(obj[key])
else:
    #строка должна быть в двойных кавычках, перед строкой должны быть "f", переменная в скобках
    print(f"ключа {key} в json нет")
