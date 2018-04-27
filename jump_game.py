class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dp = [True for _ in range(len(nums))]

        for i in range(1, len(nums)):
            dp[i] = False
            for j in reversed(range(i)):
                if nums[j] + j - i >= 0 and dp[j]:
                    dp[i] = True
                    break

        return dp[-1]
