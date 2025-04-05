
from typing import List
import sys


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    left_pointer_stock = 0
    currnet_buy_price = sys.maxsize
    for right_pointer_stock in range(len(prices)):
        if prices[right_pointer_stock] < currnet_buy_price:
            currnet_buy_price = prices[right_pointer_stock]
            left_pointer_stock = right_pointer_stock
        else:
            if prices[right_pointer_stock] - currnet_buy_price > max_profit:
                max_profit = prices[right_pointer_stock] - currnet_buy_price
    return max_profit


prices = [10, 1, 5, 6, 7, 1]
print(maxProfit(prices))

# by idorabin
