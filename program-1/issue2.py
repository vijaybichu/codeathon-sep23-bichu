def find_max_profit(prices):
    """
    Finds the maximum profit that can be made by buying and selling stocks.

    Args:
        prices (list): A list of stock prices.

    Returns:
        int: The maximum profit that can be made, or -1 if no profit can be made.
    """
    if len(prices) < 2:
        return -1
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    
    if max_profit == 0:
        return -1
    else:
        return max_profit
