import requests

ex_val = {
    "mob_and":{'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},#ok
    "mob_ios":{'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},#er
    "brw_unk":{'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},#er
    "brw_chr":{'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},#ok
    "mob_iph":{'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}#er
}

#print(ex_val["mob_and"]["platform"])
#print(type(ex_val))
# for x in ex_val:
#     print(type(ex_val[x]))


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
    del parsing_json['user_agent']
    if parsing_json != ex_val["mob_and"]:
        print("mob_and error")
    # elif parsing_json != ex_val["mob_ios"]:
    #     print("mob_iso error")
    # elif parsing_json != ex_val["brw_unk"]:
    #     print("brw_unk error")
    # elif parsing_json != ex_val["brw_chr"]:
    #     print("brw_chr error")
    # elif parsing_json != ex_val["mob_iph"]:
    #     print("mob_iph error")


mobile_android = {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}

print(mobile_android)