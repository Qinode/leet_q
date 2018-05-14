class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1:
            return 0
        else:
            dp_left = [0 for _ in range(len(s))]
            dp_right = [0 for _ in range(len(s))]
            dp = [0 for _ in range(len(s))]

            if s[0] == '(':
                dp_left[0] = 1

            max_length = 0

            for i in range(1, len(s)):
                if s[i] == '(':
                    dp_left[i] = dp_left[i - 1] + 1
                    dp_right[i] = dp_right[i - 1]
                else:
                    if dp_right[i - 1] < dp_left[i - 1]:
                        dp_right[i] = dp_right[i - 1] + 1
                        dp_left[i] = dp_left[i - 1]
                        temp = dp[i - 1] + 1
                        dp[i] = temp + dp[i - temp * 2]
                    else:
                        dp_right[i] = 0
                        dp_left[i] = 0

                    max_length = max(max_length, dp[i])

            return max_length * 2
