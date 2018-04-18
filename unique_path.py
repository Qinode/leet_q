class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == n == 1:
            return 1
        else:
            dp = [[1 for _ in range(n)] for _ in range(m)]
            for i in range(1, m):
                for j in range(1, n):
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
