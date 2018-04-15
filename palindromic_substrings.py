class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        if len(s) == 0:
            return res
        else:
            dp = [[False for _ in range(len(s))] for _ in range(len(s))]
            res = 0
            for i in reversed(range(len(s))):
                for j in range(i, len(s)):
                    if (j - i == 0 or j - i == 1) and s[i] == s[j]:
                        dp[i][j] = True
                        res += 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                        if dp[i][j]:
                            res += 1

        return res



