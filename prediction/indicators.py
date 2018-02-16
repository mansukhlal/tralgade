import pandas as pd

def get_SMA(price_df, window , Pcat = "close"):
    series = price_df[Pcat]
    sma = pd.Series(pd.rolling_mean(series, window))
    std = pd.Series(pd.rolling_std(series, window))
    return sma, std


def get_EWMA(price_df, window, Pcat = "close"):
    series = price_df[Pcat]
    EWMA = pd.Series(pd.ewma(series, span = window, min_periods= window - 1))
    return EWMA


def get_MACD(price_df, window_fast, window_slow, Pcat = "close"):
    series = price_df[Pcat]
    EMAfast = pd.Series(pd.ewma(series, span = window_fast, min_periods = window_slow - 1))
    EMAslow = pd.Series(pd.ewma(series, span = window_slow, min_periods = window_slow - 1))
    MACD = pd.Series(EMAfast - EMAslow)
    return MACD


def get_bollband(price_df, window, avg_tech = "SMA", width = 2, Pcat = "close"):
    sma, std = get_SMA(price_df=price_df, window=window, Pcat=Pcat)
    if avg_tech == "SMA":
        bollinger_ub = sma + std * width
        bollinger_lb = sma - std * width

    elif avg_tech == "EWMA":
        ewma = get_EWMA(price_df =  price_df, window=window, Pcat = Pcat)
        bollinger_ub = ewma + std * width
        bollinger_lb = ewma - std * width
    return bollinger_ub, bollinger_lb, 2 * width * std


def get_RSI(price_df, window = None, avg_tech = "EWMA", Pcat = "close"):
    series = price_df[Pcat]
    delta = series.diff()[1:]
    p_gain, n_gain = delta.copy(), delta.copy()
    p_gain[p_gain < 0] = 0
    n_gain[n_gain > 0] = 0

    if avg_tech == "EWMA":
        roll_up = pd.stats.moments.ewma(p_gain, window)
        roll_down = pd.stats.moments.ewma(n_gain.abs(), window)
    elif avg_tech == "SMA":
        roll_up = pd.rolling_mean(n_gain, window)
        roll_down = pd.rolling_mean(n_gain.abs(), window)

    rs = roll_up / roll_down
    RSI = 100.0 - (100.0 / (1.0 + rs))
    return RSI


def is_bullish_engulfing(self, candle_prev, candle_next, bollinger_lb):
    if candle_next.close - candle_next.open > 0:
        bb_outpercent = (bollinger_lb - candle_prev.close) / (candle_prev.open - candle_prev.close)
        engulf_ratio = (candle_next.close - candle_next.open)/(candle_prev.open - candle_prev.close)
        if bb_outpercent > 0.3 and engulf_ratio > 1.3:
            return True
        else:
            return False
    else:
        return False



def is_bearish_engulfing(self, candle_prev, candle_next, bollinger_ub):
    if candle_next.close - candle_next.open < 0:
        bb_outpercent = (candle_prev.close - bollinger_ub) / (candle_prev.close - candle_prev.open)
        engulf_ratio = (candle_next.open - candle_next.close) / (candle_prev.close - candle_prev.open)
        if bb_outpercent > 0.3 and engulf_ratio > 1.3:
            return True
        else:
            return False
    else:
        return False


def is_doji_break(self, last2_candles, current_candle):
    is_doji = 0
    for index, rows in last2_candles.iterrows():
        if 0.002 > 1 - (rows.close/rows.open) > -0.002:
            is_doji +=1
    if is_doji == 2 and abs(1 - current_candle.open/current_candle.close) > 0.01:
        return True
    else:
        return False




def is_doji_hammer(self, ):
    pass


def market_trend(self):
    pass



def get_supertrend(self):
    # series_high, series_low = self.price_df["hig"], self.price_df["low"]
    # i = 0
    # TR_l = [0]
    # while i < len(df) - 1:
    #     TR = max(df['High'].iloc[i + 1], df['Close'].iloc[i] - min(df['Low'].iloc[i + 1], df['Close'].iloc[i]))
    #     TR_l.append(TR)
    #     i = i + 1
    # TR_s = pd.Series(TR_l)
    # result = pd.Series(pd.ewma(TR_s, span=n, min_periods=n), name='ATR_' + str(n))
    print "Super trend indicator is yet to be implemented..."


def get_stoc_oscilator(self):
    print "Stochastic Oscilator is yet to be implemented..."


