import sys


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sold = 0
        rest = 0
        hold = -sys.maxsize
        for price in prices:
            prev_sold = sold
            sold = hold + price
            hold = max(hold, rest - price)
            rest = max(rest, prev_sold)

        return max(rest, sold)