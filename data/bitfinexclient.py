import requests
import config
import Queue
import websocket
from threading import Thread
import json
import time
import types
from datetime import datetime
import string


class CandleStick:

    def __init__(self):
        self.opening = 0
        self.closing  = 0
        self.high = 0
        self.low = 0

    def put_values(self, opening = 0, closing = 0, high = 0, low = 0):
        self.opening = opening
        self.closing = closing
        self.high = high
        self.low = low


class WebSocketDataClient:

    def __init__(self, entity1 = "BTC", entity2 = "USD"):
        self.q = Queue.Queue(maxsize=1000)
        self.entity1, self.entity2 = entity1, entity2
        print "WebSocket data client created"

    def async_connection(self):
        async_connect = Thread(target=self.connect)
        async_connect.start()

    def connect(self):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("wss://api.bitfinex.com/ws/2", on_message=self.on_message, on_error=self.on_error, on_close=self.on_close)
        ws.on_open = self.on_open
        ws.run_forever()

    def format_data(self, value_list):
        data_dict = {}
        data_dict["timestamp"] = str(datetime.now()).translate(None, string.punctuation).replace(' ', '')[:-6]
        key_list = ["CHANNEL_ID", ["BID", "BID_SIZE", "ASK", "ASK_SIZE", "DC", "DCP", "LP", "VOL", "HIGH", "LOW"]]
        if type(value_list) is not list:
            return None
        elif isinstance(value_list[1], types.StringTypes):
            return None
        elif len(key_list[1]) == len(value_list[1]):
            for iter in range(len(key_list[1])):
                data_dict[key_list[1][iter]] = value_list[1][iter]
            return data_dict

    def on_message(self, ws, message):
        data = self.format_data(json.loads(message))
        if data:
            self.q.put(data)

    def on_error(self, ws, error):
        print "Error in connection: ", error

    def on_close(self, ws):
        print "connection was closed, retrying to connect in a seconds"
        time.sleep(1)
        self.async_connection()

    def on_open(self, ws):
        msg = {'event': 'subscribe', 'channel': 'ticker', 'symbol': 'tBTCUSD'}
        ws.send(json.dumps(msg))


class RestDataClient:

    def __init__(self):
        print "data client created..."

    def getCurrentStatus(self, entity1 = "BTC", entity2 = "USD"):
        symbol = config.Symbols(entity1, entity2)
        url = "https://api.bitfinex.com/v1/pubticker/" + symbol
        response = requests.request("GET", url)
        attribute_dict = json.loads(response.text)
        return attribute_dict

    def getRecentTrades(self, entity1 = "BTC", entity2 = "USD"):
        symbol = config.Symbols(entity1, entity2)
        url = "https://api.bitfinex.com/v1/trades/" + symbol
        response = requests.request("GET", url)
        attribute_dict = json.loads(response.text)
        return attribute_dict


class TransactionClient():

    def __init__(self):
        print "work is still in progress for transaction client.."
        pass


    def purchase(self, enity1 = "btc", entity2 = "usd", quantity = 0.001):
        '''make actual purchase on bitfinex using account holder api'''
        print "work in progress"

    def sell(self, enity1 = "btc", entity2 = "usd"):
        '''sell out the desire amount'''
        print "work in progress"

    def short_sell(self, enity1 = "btc", entity2 = "usd"):
        '''short desired amout'''



#this is code block for testing the functions in the RestDataClient class:
#
# client = DataClient()
# for i in range(10):
#     print client.getCurrentStatus(entity1="BTC", entity2="USD")
#     time.sleep(10)
#print client.getRecentTrades(entity1="BTC", entity2="USD")



# This code is for testing WebSocketDataClient
# wsdc = WebSocketDataClient()
# wsdc.async_connection()
# while True:
#     try:
#         print "Printed from the try/catch loop: ", wsdc.q.get()
#     except Queue.Empty:
#         print "The queue is empty, wait for some time"
#         time.sleep(10)
#