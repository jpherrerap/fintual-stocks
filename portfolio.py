from datetime import datetime

class Stock:
    """A stock.
    
    Attributes:
        symbol (str): The symbol of the stock.
        prices (dict): A dictionary of dates and prices.
        quantity (int): The quantity of the stock.
    """

    def __init__(self, symbol: str, quantity: int):
        """
        Initialize a stock.

        Args:
            symbol (str): The symbol of the stock.
            quantity (int): The quantity of the stock.
        """
        self.symbol = symbol
        self.prices = {}
        self.quantity = quantity
        
    def price(self, date: datetime) -> float:
        """
        Get the price of the stock on a given date.

        Args:
        date (datetime): The date to get the price for.

        Returns:
            float: The price of the stock on the given date.
        """
        return self.prices.get(date, 0)



class Portfolio:
    """
    A portfolio of stocks.
    """

    def __init__(self):
        self.stocks: dict[str, Stock] = {}

    def add_stock(self, stock: Stock):
        """
        Add a stock to the portfolio.

        Args:
            stock (Stock): The stock to add.
        """
        self.stocks[stock.symbol] = stock

    def get_value(self, date: datetime) -> float:
        """
        Get the value of the portfolio on a given date.

        Args:
            date (datetime): The date to get the value for.

        Returns:
            float: The value of the portfolio on the given date.
        """
        return sum(stock.price(date) * stock.quantity for stock in self.stocks.values())

    def profit(self, start_date: datetime, end_date: datetime, annualized: bool = False) -> float:
        """
        Get the profit of the portfolio between two dates.

        Args:
            start_date (datetime): The start date.
            end_date (datetime): The end date.
            annualized (bool): Whether to return the annualized return
        Returns:
            float: The profit of the portfolio between the two dates.
        """

        if start_date >= end_date:
            raise ValueError("Start date cannot be after end date")
        
        profit = self.get_value(end_date) - self.get_value(start_date)
        
        if not annualized:
            return profit

        total_return = profit / self.get_value(start_date)
        days = (end_date - start_date).days
        
        if days == 0:
            return 0
        
        annualized_return = (1 + total_return) ** (365 / days) - 1
        return annualized_return
