# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 23:25:02 2020

@author: Gigabyte
"""

import math
import backtrader as bt

# extends bt.Strategy
class GoldenCross(bt.Strategy):
    params = (
            ('fast', 50),
            ('slow', 200),
            # Only 95% invested
            ('order_percentage', 0.95),
            ('ticker', 'SPY')
            )
    
    def __init__(self):
        self.fast_moving_average = bt.indicators.SMA(
                self.data.close, period = self.params.fast,
                plotname ='50MA'
                )
        
        self.slow_moving_average = bt.indicators.SMA(
                self.data.close, period = self.params.slow,
                plotname = '200MA'
                )
        
        #Refer to Crossover Documentation 
        # +1 if 1day cross 2day , -1 if 2 day cross 1 day
        # Decides if golden cross of death cross
        self.crossover = bt.indicators.CrossOver(self.fast_moving_average,
                                                 self.slow_moving_average)
        
    def next(self):
        # Check position size because we going to invest up to 95% of our portfolio size
        if self.position.size == 0:
            #if position size of SPY = 0 
            if self.crossover > 0:
                amount_to_invest = (self.params.order_percentage *
                                    self.broker.cash)
                
                #max size is equals rounded down value of investable
                self.size = math.floor(amount_to_invest/ self.data.close)
                
                print("BUY {} shares of {} at {}".format(self.size,
                                                          self.params.ticker,
                                                          self.data.close[0]))
                
                self.buy(size =self.size)
                
        if self.position.size > 0:
            if self.crossover < 0:
                print("SELL {} shares of {} at {}".format(self.size,
                                                          self.params.ticker,
                                                          self.data.close[0]))
                self.close()