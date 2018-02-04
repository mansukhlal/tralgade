from datetime import datetime
import time
import MySQLdb
from sys import argv
import Queue
from bitfinexclient import RestDataClient, WebSocketDataClient, CandleStick


class DataLogger:
    '''
    Use of candlesticks is redundant, should be removed. Use single row dataframes or dictionary in its place.
    '''

    def __init__(self, entity1 = "BTC", entity2 = "USD"):
        self.client = WebSocketDataClient()
        #   in future, the DB info will be fetched from config file
        self.db_connection = MySQLdb.connect(host="localhost", user="root", passwd="junkyard", db="Tralgade_Candles")
        self.entity1 = entity1
        self.entity2 = entity2
        self.create_data_table()

    def create_data_table(self):
        cur = self.db_connection.cursor()
        stmt = "CREATE TABLE IF NOT EXISTS candlesticks_" + self.entity1 + "_" +self.entity2+ " (timestamp varchar(20), opening float, closing float, high float, low float, volume float, change_perc float);"
        cur.execute(stmt)

    def _get_candles(self, duration=60):
        new_candlestick = CandleStick()
        data = []
        start_time, time_elapsed = time.time(), 0
        while time_elapsed <= duration:
            try:
                cdata = self.client.q.get(False)
            except Queue.Empty:
                time.sleep(3)
            except Exception as err:
                print err
                with open("Error_DataLogger.log", 'a') as errorlogs:
                    errorlogs.write("could not get data from the exchange at time: " + str(datetime.now()) + "\n")
            else:
                price = cdata["ASK"] / 2.0 + cdata["BID"] / 2.0
                data.append(float(price))
            time_elapsed = time.time() - start_time
        new_candlestick.put_values(opening=str(data[0]), closing=str(data[-1]), high=str(max(data)), low=str(min(data)))
        print "candlestick created in sec: ", time_elapsed
        return cdata["timestamp"], new_candlestick

    def log(self):
        cur = self.db_connection.cursor()
        self.client.async_connection()
        while True:
            time_stamp, candle = self._get_candles(duration=60)
            stmt = "INSERT INTO candlesticks_" + self.entity1 + "_" + self.entity2  + " (timestamp, opening, closing, high, low) VALUES (%s, %s, %s, %s, %s);" % (str(time_stamp), candle.opening, candle.closing, candle.high, candle.low)
            response = cur.execute(stmt)
            print "response: ", response
            self.db_connection.commit()


if __name__ == "__main__":
    logger = DataLogger(entity1=argv[1], entity2=argv[2])
    logger.log()

