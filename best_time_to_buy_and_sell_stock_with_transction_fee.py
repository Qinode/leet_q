import sys
class Solution:
    def maxProfit(self, prices, fee):
        s0, s1 = 0, -sys.maxsize;
        for p in prices:
            s0 = max(s0, s1+p);
            s1 = max(s1, s0-p-fee);
        return s0

    def maxProfit_time_exceed(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp = [0 for _ in range(len(prices))]

        for i in range(1, len(prices)):
            max_profit = dp[i - 1]
            for j in range(i):
                max_profit = (max_profit, prices[i] - prices[j] - fee)

            dp[i] = max_profit
        return dp[-1]
