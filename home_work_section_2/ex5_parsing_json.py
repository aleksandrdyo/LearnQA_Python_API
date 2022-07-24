import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

#json.loads переводит JSON в объекты Python.
parsed_json = json.loads(json_text)

messages = parsed_json['messages']

message2 = messages[1]

print(message2['message'])

# for x in messages:
#     print(x['message'])
