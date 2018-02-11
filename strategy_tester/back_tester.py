from data_center import DataRetriever
import indicators
import pandas as pd


def generate_signals(ind_df, sorted_df):
    print "generating signals for th e data provided"
    signal_list = []
    for index, row in ind_df.iterrows():
        if (row["MACD"] > 0 and row["bolb_diff"] > 50 and row["RSI"] > 70):
            signal_list.append("buy")
        elif (row["MACD"] < 0 and row["bolb_diff"] < 10 and row["RSI"] < 30):
            signal_list.append("sell")
        else:
            signal_list.append("wait for the moment")
    signal_df = pd.DataFrame({"trade_signals": signal_list})
    sorted_df["trade signals"] = signal_df
    return sorted_df


class back_tester:

    def __init__(self):
        self.wallet = {"BTC":0, "USD":0, "ETH":0, "IOTA":0, "Neo":0, "XRP":0, "ETC":0}
        print "wallet created for back testing..."

    def build_indicators(self):
        df = pd.read_csv("/home/kbz/Downloads/btcusd-candles (1).csv")
        sorted_df = df.sort_values(by='timestamp')
        indicator_df = pd.DataFrame()
        indicator_df["time_stamp"] = sorted_df["timestamp"]

        SMA, STD = indicators.get_SMA(price_df=sorted_df, window = 20)
        indicator_df["SMA"] = SMA
        print "SMA for the given data is: "
        print SMA.tail(10)

        EWMA = indicators.get_EWMA(price_df=sorted_df, window=20)
        indicator_df["EWMA"] = EWMA
        print "EWMA for the given data is: "
        print EWMA.tail(10)

        MACD = indicators.get_MACD(price_df=sorted_df, window_fast=10, window_slow=20)
        indicator_df["MACD"] = MACD
        print "MACD for the given data is: "
        print MACD.tail(10)

        bol_ub, bol_lb, bolb_diff = indicators.get_bollband(price_df=sorted_df, window = 20, width=2)
        indicator_df["bol_ub"] = bol_ub
        indicator_df["bol_lb"] = bol_lb
        indicator_df["bolb_diff"] = bolb_diff
        print "Bollinger upper-band for the given data is: "
        print bol_ub.tail(10)
        print "Bollinger lower-band for the given data is: "
        print bol_lb.tail(10)
        print "Bollinger bands difference for the given data is: "
        print bolb_diff.tail(10)


        RSI = indicators.get_RSI(price_df=sorted_df, window=20, avg_tech="EWMA")
        indicator_df["RSI"] = RSI
        print "RSI for the given data is: "
        print RSI.tail(10)

        print indicator_df.tail(20)


dfWsignal = generate_signals(ind_df = indicator_df, sorted_df=sorted_df)
print dfWsignal.tail(30)
dfWsignal.to_csv("/home/kbz/Downloads/trade_signal.csv", sep=',')