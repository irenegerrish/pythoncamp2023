# Homework 1: due August 18, 2023
# Author: Irene Gerrish

import random

class Portfolio:
    def __init__(self, client_id, cash_balance=0, mutual_fund=0, stocks=0):
        self.client = Client(client_id, cash_balance, mutual_fund, stocks)
        self.Stocks = []
        self.MutualFunds = []
        self.withdrawCash = []
        self.balance = 0

    def addCash(self, cash):
        self.balance += cash
        print(self.balance)

    def history(self):
        return self.balance, self.withdrawCash, self.mutual_fund, self.stock

class MutualFund:
    def __init__(self, mutual_fund):
        self.mutual_fund = mutual_fund
        self.randomprice = random.uniform(0.9, 1.2)

    def buyMutualFund(self, amount):
        self.buyMutualFund += buyMutualFund
        self.amount = amount

    def sellMutualFund(self, amount):
        self.sellMutualFund -= sellMutualFund
        self.amount = amount

class Stock:
    def __init__(self, stock):
        self.stock = stock

    def buyStock(self, stock):
        self.buyStock = buyStock 

    def sellStock(self, stock, cash):
        self.sellStock += stock
        self.withdrawCash -= cash
        return self.sellStock + self.withdrawCash

# Commands to run

portfolio = Portfolio() # creates new portfolio
portfolio.addCash(300.50) # adds cash to portfolio
portfolio.withdrawCash(50) # withdraw $50 from cash
stock = Stock(20, 'HFH') # creates new stock
portfolio.buyStock(5, stock) # buys 5 shares of stocks 
mf1 = MutualFund('BRT') # creates mutual fund called 'BRT'
mf2 = MutualFund('GHT') # creates mutual fund called 'GHT'
portfolio.buyMutualFund(10.3, mf1) # buy 10.3 shares of BRT
portfolio.buyMutualFund(2, mf2) # buy 2 shares of GHT
portfolio.sellMutualFund('BRT', 3) # sell 3 shares of BRT
portfolio.sellMutualFund('HFH', 1) # sell 1 share of HFH
portfolio.history() # prints transaction history    
