import requests
import json
import fake_useragent


class Bing(object):
    def _random_headers(self):
        headers = {
            "dnt": "1",
            "user-agent": fake_useragent.UserAgent().random,
            "origin": "https://cn.bing.com",
            "referer": "https://www.bing.com/translator",
        }
        return headers

    def __init__(self, lang_from="en", lang_to="zh"):
        self.lang_from = lang_from
        self.lang_to = lang_to
        self.sess = requests.Session()

    def translate(self, text):
        url = "https://cn.bing.com/ttranslate?&category=&IID=translator.5038.11"

        try:
            response = self.sess.post(
                url,
                data={"text": text, "from": self.lang_from, "to": self.lang_to},
                headers=self._random_headers(),
                timeout=1,
            )
        except Exception:
            return None

        if len(response.text) == 0:
            return None

        result = json.loads(response.text)

        if "translationResponse" not in result:
            return None

        return result["translationResponse"]
