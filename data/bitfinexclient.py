import requests
import json


class DataClient:
    def __init__(self):
        print("data client created...")

    @staticmethod
    def _get_symbol(x, y):
        return y + x

    def get_status(self, x="BTC", y="USD"):
        response = requests.get("https://api.bitfinex.com/v1/pubticker/" + self._get_symbol(x, y))
        return json.loads(response.text)

    def get_trades(self, x="BTC", y="USD"):
        response = requests.get("https://api.bitfinex.com/v1/trades/" + self._get_symbol(x, y))
        return json.loads(response.text)
