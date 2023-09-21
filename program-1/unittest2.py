def find_max_profit(prices):
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

import unittest

class TestFindMaxProfit(unittest.TestCase):
    def test_max_profit(self):
        # Test finding the maximum profit
        prices = [7, 1, 5, 3, 6, 4]
        max_profit = find_max_profit(prices)
        self.assertEqual(max_profit, 5)
    
    def test_no_profit(self):
        # Test when no profit can be made
        prices = [7, 6, 4, 3, 1]
        max_profit = find_max_profit(prices)
        self.assertEqual(max_profit, -1)
    
    def test_single_price(self):
        # Test when there is only one price
        prices = [7]
        max_profit = find_max_profit(prices)
        self.assertEqual(max_profit, -1)
    
    def test_increasing_prices(self):
        # Test when prices are increasing
        prices = [1, 2, 3, 4, 5]
        max_profit = find_max_profit(prices)
        self.assertEqual(max_profit, 4)
    
    def test_decreasing_prices(self):
        # Test when prices are decreasing
        prices = [5, 4, 3, 2, 1]
        max_profit = find_max_profit(prices)
        self.assertEqual(max_profit, -1)

if __name__ == '__main__':
    unittest.main()
