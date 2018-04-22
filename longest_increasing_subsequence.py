class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sort_nums = sorted(nums)
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            dp = [[0 for _ in range(len(nums) + 1)] for _ in range(len(nums) + 1)]

            for i in range(1, len(nums) + 1):
                dp[i][0] = dp[0][i] = i

            for i in range(1, len(nums) + 1):
                for j in range(1, len(nums) + 1):
                    if sort_nums[i - 1] == nums[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

            print(dp)
            return len(nums) - dp[-1][-1]


