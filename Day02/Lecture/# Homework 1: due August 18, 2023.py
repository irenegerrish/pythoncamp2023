# Homework 1: due August 18, 2023
# Author: Irene Gerrish

class Client:
    def __init__(self, client_id, cash_balance, mutual_funds, stocks):
        self.client_id = client_id
        self.cash_balance = cash_balance
        self.mutual_funds = mutual_funds
        self.stocks = stocks

    def calculate_portfolio_value(self):
        return self.cash_balance + self.mutual_funds + self.stocks

    def buy_mutual_funds(self, amount):
        self.mutual_funds += amount
        self.cash_balance -= amount

    def sell_stocks(self, amount):
        self.stocks -= amount
        self.cash_balance += amount

class Portfolio:
    def __init__(self, client_id, cash_balance=0, mutual_funds=0, stocks=0):
        self.client = Client(client_id, cash_balance, mutual_funds, stocks)

Portfolio()