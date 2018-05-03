import sys

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        profit = 0
        minimum = prices[0]
        maximum = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                if maximum > minimum:
                    profit += maximum - minimum

                minimum = prices[i]
                maximum = prices[i]

            if prices[i] > maximum:
                maximum = prices[i]
            else:
                profit += max(maximum - minimum, 0)
                maximum = prices[i]
                minimum = prices[i]

        return profit + max(maximum - minimum, 0)
