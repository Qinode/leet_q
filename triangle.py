class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 1:
            return triangle[0][0]
        else:
            dp = [triangle[0]]
            for i in range(1, len(triangle)):
                row = [triangle[i][0] + dp[i - 1][0]]
                for j in range(1, len(triangle[i]) - 1):
                    row.append(min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j])
                row.append(dp[i - 1][-1] + triangle[i][-1])
                dp.append(row)

        return min(dp[-1])
