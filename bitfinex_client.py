import requests
import config

class data_client:

    def __init__(self):
        print "data client created..."

    @staticmethod
    def text_to_dict(text):
        attribute_list = str(text)[1:-2].split(',')
        attribute_dict = {}
        for attribute in attribute_list:
            key, value = attribute.split(':')
            attribute_dict[key.strip('"')] = value.strip('"')
        return attribute_dict

    def get_current_status(self, entity1 = "BTC", entity2 = "USD"):
        symbol = config.Symbols(entity1, entity2)
        url = "https://api.bitfinex.com/v1/pubticker/" + symbol
        response = requests.request("GET", url)
        attribute_dict = self.text_to_dict(response.text)
        return attribute_dict

    def get_recent_trades(self, entity1 = "BTC", entity2 = "USD"):
        symbol = config.Symbols(entity1, entity2)
        url = "https://api.bitfinex.com/v1/trades/" + symbol
        response = requests.request("GET", url)
        attribute_dict = self.text_to_dict(response.text)
        return attribute_dict


class transaction_client():

    def __init__(self):
        print "work is still in progress for transaction client.."
        pass

    def simul_purchase(self, entity1 = "btc", entity2 = "usd"):
        '''make simulated purchase and make entry in db'''

    def simul_sell(self, entity1="btc", entity2 = "usd"):
        '''make simulated purchase and make entry in db'''

    def make_purchase(self, enity1 = "btc", entity2 = "usd", quantity = 0.001):
        '''make actual purchase on bitfinex using account holder api'''
        print "work in progress"

    def sell_out(self, enity1 = "btc", entity2 = "usd"):
        '''sell out the desire amount'''
        print "work in progress"

    def short_sell(self, enity1 = "btc", entity2 = "usd"):
        '''short desired amout'''



client = data_client()
print client.getCurrentStatus(entity1="BTC", entity2="USD")
print client.getRecentTrades(entity1="BTC", entity2="USD")
