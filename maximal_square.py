class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if len(matrix) == 0:
            return 0
        elif len(matrix) == 1 and len(matrix[0]) == 1:
            return int(matrix[0][0])
        else:
            maximal = 0
            dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

            for i in range(len(matrix)):
                dp[i][0] = int(matrix[i][0])
                maximal = max(maximal, dp[i][0])

            for i in range(len(matrix[0])):
                dp[0][i] = int(matrix[0][i])
                maximal = max(maximal, dp[0][i])

            for i in range(1, len(matrix)):
                for j in range(1, len(matrix[i])):
                    if matrix[i][j] == '0':
                        dp[i][j] = 0
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

                    maximal = max(maximal, dp[i][j])

        return maximal * maximal
