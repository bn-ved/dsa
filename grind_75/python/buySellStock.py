from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, lowest_buy = 0, prices[0]
        for price in prices:
            if price < lowest_buy:
                lowest_buy = price
            else:
                profit = max(profit, price - lowest_buy)

        return profit
