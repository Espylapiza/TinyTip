import requests
import json
import fake_useragent


def get_translation(text):
    url = "https://cn.bing.com/ttranslate"

    headers = {
        "user-agent": fake_useragent.UserAgent().random,
        "origin": "https://cn.bing.com",
        "referer": "https://cn.bing.com/search",
    }

    response = requests.post(
        url, data={"text": text, "from": "en", "to": "zh-CHS"}, headers=headers
    )

    if len(response.text) == 0:
        return None

    print(response.text)

    result = json.loads(response.text)

    if "translationResponse" not in result:
        return None

    return result["translationResponse"]
