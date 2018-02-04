'''
uses following SQL tables for storing data of assets holding and Transactions done
1) Tralgade_PaperTrade.ASSETS(symbol varchar(10), name varchar(20), amount float, PRIMARY KEY(symbol));
2) Tralgade_PaperTrade.Transactions(timestamp varchar(20), InCurrency varchar(10), InCurrencyAmount float , OutCurrency varchar(10), OutCurrencyAmount float, TransactionMode varchar(20), PRIMARY KEY (timestamp));
'''

from datetime import datetime
import MySQLdb
from threading import Thread

# this file holds dummy traders bots for paper trading

class Dummy_Trader:
    Assets = {}

    def __init__(self):
        db_connection = MySQLdb.connect(host="localhost", user="root", passwd="junkyard", db="Tralgade_PaperTrade")
        self.cur = db_connection.cursor()
        self.balance = 0
        self.get_current_assets()
        print "a new trader has been created.."

    def get_current_assets(self):
        stmt = "SELECT * FROM ASSETS;"
        try:
            self.cur.execute(stmt)
            results = self.cur.fetchall()
            for row in results:
                Dummy_Trader.Assets[row[0]] = row[2]
        except Exception as err:
            print "could not fetch data from the Asset Table.. invalid object created"


    def limit_buy(self, InCurrency, price, amount, OutCurrency, brokerage = 0.1):
        if Dummy_Trader.Assets[InCurrency] >= amount:
            transact_amt = amount * (1 + brokerage/100) * price
            Dummy_Trader.Assets[InCurrency]-=transact_amt
        asset_stmt = "INSERT INTO"

        return True


    def limit_sell(self, amount, price):
        transanct_amt = price * amount

        pass

    def market_buy(self, amount):
        pass

    def market_sell(self, amount):
        pass




trader = Dummy_Trader()
print trader.Asstets