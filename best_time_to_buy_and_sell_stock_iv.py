import sys


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        if k == 0:
            return 0
        elif k > len(prices):
            i = 0
            max_profit = 0
            while i < len(prices) - 1:
                while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                    i += 1
                valley = prices[i]

                while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                    i += 1
                peak = prices[i]

                max_profit += (peak - valley)
            return max_profit
        else:
            sell = [0 for i in range(k)]
            buy = [-sys.maxsize for i in range(k)]

            for price in prices:
                buy[0] = max(buy[0], - price)
                sell[0] = max(sell[0], buy[0] + price)
                for i in range(1, k):
                    buy[i] = max(buy[i], sell[i - 1] - price)
                    sell[i] = max(sell[i], buy[i] + price)

            return sell[-1]