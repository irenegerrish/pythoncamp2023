# Homework 1: due August 18, 2023
# Author: Irene Gerrish

class Client:
    def __init__(self, client_id, cash_balance, mutual_funds, stocks):
        self.client_id = client_id
        self.cash_balance = cash_balance
        self.mutual_funds = mutual_funds
        self.stocks = stocks
        portfolio = self.cash_balance + self.mutual_funds + self.stocks


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



# Example usage
client_id = 1
portfolio = clients.get(client_id)
if portfolio:
    print("Original Portfolio:")
    print("Cash Balance:", portfolio.client.cash_balance)
    print("Mutual Funds:", portfolio.client.mutual_funds)
    print("Stocks:", portfolio.client.stocks)

    # Buy $1000 worth of mutual funds
    portfolio.client.buy_mutual_funds(1000)
    print("Portfolio after buying mutual funds:")
    print("Cash Balance:", portfolio.client.cash_balance)
    print("Mutual Funds:", portfolio.client.mutual_funds)
    print("Stocks:", portfolio.client.stocks)

    # Sell $2000 worth of stocks
    portfolio.client.sell_stocks(2000)
    print("Portfolio after selling stocks:")
    print("Cash Balance:", portfolio.client.cash_balance)
    print("Mutual Funds:", portfolio.client.mutual_funds)
    print("Stocks:", portfolio.client.stocks)
else:
    print("Client not found.")