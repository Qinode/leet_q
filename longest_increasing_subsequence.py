class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            dp = [1 for _ in range(len(nums))]
            max_len = 1

            for i in range(1, len(nums)):
                max_val = 0
                for j in range(i):
                    if nums[i] > nums[j]:
                        max_val = max(max_val, dp[j])
                dp[i] = max_val + 1
                max_len = max(max_len, dp[i])
            return max_len


