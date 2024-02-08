import yfinance as yahooFinance


def getStockValue(symbol, quantity):
    stock = yahooFinance.Ticker(symbol)
    current_price = stock.info['currentPrice']
    return current_price * quantity


def getPortfolioValue(stocks):
    total_value = sum(getStockValue(
        stock['symbol'], stock['quantity']) for stock in stocks)
    return total_value


stocks = [
    {"symbol": "AAPL", "quantity": 43},
    {"symbol": "GOOG", "quantity": 65},
    {"symbol": "TSLA", "quantity": 52},
]

portfolio_value = getPortfolioValue(stocks)

print("Portfolio Status:")
for stock in stocks:
    stock_value = getStockValue(stock['symbol'], stock['quantity'])
    print(
        f"Holding {stock['quantity']} shares of {stock['symbol']}, Total value: {stock_value}")

print(f"Total portfolio value: {portfolio_value}")