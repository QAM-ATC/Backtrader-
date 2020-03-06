import os, sys, argparse
import pandas as pd
import backtrader as bt
from strategies.GoldenCross import GoldenCross
from strategies.BuyHold import BuyHold


strategies = {
        "golden_cross": GoldenCross,
        "buy_hold" : BuyHold
        }

parser = argparse.ArgumentParser()
parser.add_argument("strategy",  help="which strategy to run", type =str)
args = parser.parse_args()


if not args.strategy in strategies:
    print("Invalid Strategy, must be one of {}".format(strategies.keys()))
    sys.exit()


cerebro = bt.Cerebro()
#SET CASH TO 100000
cerebro.broker.set_cash(100000)
spy_prices = pd.read_csv('data/SPY.csv', index_col = "Date", parse_dates = True)

#Possible to integrate Yahoo Finance API at this point

feed = bt.feeds.PandasData(dataname = spy_prices)
cerebro.adddata(feed)
cerebro.addstrategy(BuyHold)
print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())
cerebro.run()
print("Ending Portfolio Value: %.2f" % cerebro.broker.getvalue())
cerebro.plot()