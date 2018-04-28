class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            dp = [1 for _ in range(n + 1)]
            dp[1], dp[2] = 1, 2

            for i in range(3, n + 1):
                dp[i] = 0
                for j in range(i):
                    dp[i] += (dp[j] * dp[i - 1 - j])

            return dp[-1]

