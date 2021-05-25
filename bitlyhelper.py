import requests


TOKEN = "b6571df03b52ebe9206ac3ef320bb3d4d5e2025d"
ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v3/shorten?access_token={}&longUrl={}"


class BitlyHelper:
    def shorten_url(self, longurl):
        try:
            url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
            response = requests.get(url)
            jr = response.json()
            return jr['data']['url']
        except Exception as e:
            return e
