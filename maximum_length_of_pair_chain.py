class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()

        if len(pairs) == 0:
            return 0
        elif len(pairs) == 1:
            return 1
        else:
            dp = [1 for _ in range(len(pairs))]
            for i in range(1, len(pairs)):
                for j in range(i):
                    if pairs[j][1] < pairs[i][0] and dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1

        max_length = 0
        for length in dp:
            if length > max_length:
                max_length = length

        return max_length
