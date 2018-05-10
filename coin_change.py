import sys


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1
        else:
            dp = [-1 for _ in range(amount + 1)]
            for i in range(1, amount + 1):
                min_change = sys.maxsize
                for coin in coins:
                    if coin > i:
                        continue
                    elif coin == i:
                        min_change = 1
                        break
                    else:
                        if dp[i - coin] != -1:
                            min_change = min(min_change, dp[i - coin] + 1)
                        else:
                            continue
                dp[i] = min_change if min_change != sys.maxsize else -1

            return dp[-1]


