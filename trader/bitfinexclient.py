from trader.client import TradeClient


class BitFinExTradeClient(TradeClient):
    def __init__(self):
        super().__init__()
        print("work is still in progress for transaction client..")

    def purchase(self, amt=0.001, x="usd", y="btc"):
        """make actual purchase on bitfinex using account holder api"""
        print("work in progress")

    def sell(self, amt=0.001, x="usd", y="btc"):
        """sell out the desire amount"""
        print("work in progress")

    def short_sell(self, amt=0.001, x="usd", y="btc"):
        """short desired amount"""
