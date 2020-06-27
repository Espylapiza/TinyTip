import json

import fake_useragent
import requests


class Bing(object):
    def _random_headers(self):
        headers = {
            "dnt": "1",
            "user-agent": fake_useragent.UserAgent().random,
            "origin": "https://www.bing.com",
            "referer": "https://www.bing.com/translator",
        }
        return headers

    def __init__(self, lang_from, lang_to):
        self.lang_from = lang_from
        self.lang_to = lang_to
        self.sess = requests.Session()

    def translate(self, text):
        url = "https://www.bing.com/ttranslate?&category=&IG=25E4ABDE972942CDA7210CF0846A9202&IID=translator.5037.2"

        try:
            response = self.sess.post(
                url,
                data={"text": text, "from": self.lang_from, "to": self.lang_to},
                headers=self._random_headers(),
                timeout=2.5,
            )
            print(response.request.headers)
        except Exception:
            return None

        if len(response.text) == 0:
            return None

        result = json.loads(response.text)

        if "translationResponse" not in result:
            return None

        return result["translationResponse"]
