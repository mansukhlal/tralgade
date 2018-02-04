'''
build strategies including elliot wave theory, gann fan, confluence etc
'''
import pandas as pd
import indicators
from data_center import DataRetriever
from config import Confluence_config


class Confluence:
    '''
    confluence class takes outcomes of various market indicators and guess the entry and exit times
    Main indicators used here are Bollinger band, MACD, Stochastic-RSI, Exponential Moving Average, etc
    '''
    def __init__(self, config_number):
        self.indicator_df = pd.DataFrame()
        self.Indicator_params = Confluence_config(config_no=config_number)


    def get_indicator_values(self):
        retriever = DataRetriever()
        candle_dfs ={}
        for size in self.Indicator_params["csizes_required"]:
            csize = str(size)+"minutes"
            candle_dfs[csize] = retriever.fetch_data(End=0, csize=size, num_candles=40)
        if self.Indicator_params["SMA"]["stat"]:
            #calculate SMA for all candle size
            pass
        if self.Indicator_params["EWMA"]["stat"]:
            #calculate SMA for all candle size
            pass
        if self.Indicator_params["MACD"]["stat"]:
            #calculate SMA for all candle size
            pass
        if self.Indicator_params["bollband"]["stat"]:
            #calculate SMA for all candle size
            pass
        if self.Indicator_params["RSI"]["stat"]:
            #calculate SMA for all candle size
            pass
        if self.Indicator_params["S_RSI"]["stat"]:
            #calculate SMA for all candle size
            pass

    def is_buy_signal(self):
        return False

    def is_sell_signal(self):
        return False


class price_action:

    def __init__(self):
        pass

    def is_bullish_engulfing(self, candle_prev, candle_next, bollband):
        pass

    def is_bearish_engulfing(self, candle_prev, candle_next, bollband):
        pass

    def is_doji_break(self, last4_candles, bollband):
        pass

    def is_doji_hammer(self, ):
        pass

    def market_trend(self):
        pass




class ElliotWave:

    def __init__(self):
        pass


class GannFan:

    def __init__(self):
        pass


#
# {"wd_SMA":0, "csize_SMA":0, "wd_EWMA":0, "csize_EWMA":0, "wdf_MACD":0, "wds_MACD":0,
#                                  "wd_BB":0, "csize_BB":0, "wd_RSI":0, "csize_RSI":0}