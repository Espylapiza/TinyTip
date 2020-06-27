from textblob import TextBlob


class TextBlobTranslator(object):
    def __init__(self, lang_from, lang_to):
        self.lang_from = lang_from
        self.lang_to = lang_to

    def translate(self, text):
        blob = TextBlob(text)
        try:
            return blob.translate(to=self.lang_to).raw
        except Exception:
            return text
