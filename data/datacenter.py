"""
Task of this module:
1) Get data from the bitfinex client and manage it in csv files
2) Retrieve data from csv files and provide it prediction module in desired format
"""

import pandas as pd
import MySQLdb
from datetime import datetime, timedelta
import string


class DataRetriever:

    def __init__(self, entity1 = "BTC", entity2 = "USD"):
        self.db_connection = MySQLdb.connect(host="localhost", user="root", passwd="junkyard", db="Tralgade_Candles")
        self.entity1 = entity1
        self.entity2 = entity2

    def gen_sql_stmt(self, start_time, end_time):
        print "start time is: ", start_time
        Stimestamp = str(datetime.now() - timedelta(minutes = start_time)).translate(None, string.punctuation).replace(' ','')[:-6]
        Etimestamp = str(datetime.now() - timedelta(minutes=end_time)).translate(None, string.punctuation).replace(' ','')[:-6]
        sql_statement = "SELECT * FROM candlesticks_" + self.entity1 + "_" + self.entity2 + " WHERE timestamp > " +  Stimestamp  + " AND timestamp < " + Etimestamp
        print "sql statement is: ", sql_statement
        return sql_statement

    def candle_magnification(self, df, csize):
        high = []
        low = []
        counter = 0
        df_magnified = pd.DataFrame({"timestamp": [],"opening": [], "closing": [], "high": [], "low": []})
        for index, row in df.iterrows():
            if counter == 0:
                open = row["opening"]
            if 0 <= counter <= csize - 1:
                high.append(row["high"])
                low.append(row["low"])
                counter += 1
            if counter == csize:
                counter = 0
                close = row["closing"]
                candle = pd.DataFrame({"timestamp":row["timestamp"], "opening": [open], "closing": [close], "high": [max(high)], "low": [min(low)]})
                df_magnified = df_magnified.append(candle)
        return df_magnified

    def read_data(self, stmt):
        df = pd.read_sql_query(stmt, self.db_connection)
        return df

    def fetch_data(self, End = 0, csize = 1, num_candles = 10):
        Start = End + csize * num_candles                      #number of one minute candles taken for calculations
        df = self.read_data(self.gen_sql_stmt(Start, End))
        print df
        if csize == 1:
            return df
        if csize >= 1:
            return self.candle_magnification(df, csize)
        else:
            return False



class morphers:

    def __init__(self):
        pass



#test code for data retriever

# retriever = DataRetriever()
# print "dataframe for 1 minute candle:"
# print retriever.fetch_data(End = 0, csize = 1)
# print "dataframe for 3 minute candle:"
# print retriever.fetch_data(End = 0, csize = 10)
# print "dataframe for 5 minute candle:"
# print retriever.fetch_data(End = 0, csize = 15)