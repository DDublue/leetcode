from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n)
        # space: O(1)

        profit = 0
        min_price = prices[0]
        for i, curr_price in enumerate(prices[1:]):
            # curr_price may be higher than before, so more profit
            profit = max(profit, curr_price-min_price)

            # new min_price guarantees max profit with subsequent prices
            min_price = curr_price if curr_price < min_price else min_price
        return profit
