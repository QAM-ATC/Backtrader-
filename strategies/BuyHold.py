# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 23:44:34 2020

@author: Gigabyte
"""

import backtrader as bt
class BuyHold(bt.Strategy):
    
    def next(self):
        if self.position.size == 0:
            # Assuming all in and round down
            size = int(self.broker.getcash()/ self.data)
            # We buy
            self.buy(size = size)
                