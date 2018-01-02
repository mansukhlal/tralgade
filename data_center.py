import pandas as pd
import time
from bitfinex_client import data_client

"""
Task of this module:
1) Get data from the bitfinex client and manage it in csv files
2) Retrieve data from csv files and provide it prediction module in desired format
"""


class DataRetriever:

    def __init__(self):
        pass

    def get_data_lake(self, start_time, end_time):
        pass

    def data_magnification(self, df, mag):
        pass

    def read_data(self):
        pass

    def get_major_swings(self):
        pass



class DataLogger:
    def __init__(self, client):
        self.mappers = []
        self.client = client

    def _get_candles(self):
        # client.getData() then convert to candle and yield
        pass

    def _save(self):
        pass

    def log(self):
        # use time.ctime for putting in the data into the file
        # for candle in _get_candles
        # get df and run mapper
        # save

    def register_mapper(self, mappers):
        self.mappers += mappers




def get_major_swings(self, candles):
    pass

def get_market_turns(self, candles):
    pass

dl = DataLogger()
dl.register_mapper([get_major_swings, get_market_turns])