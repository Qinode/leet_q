class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(self.rob_i(nums[:-1]), self.rob_i(nums[1:]))

    def rob_i(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            dp = [nums[0] for _ in range(len(nums))]
            for i in range(1, len(nums)):
                if i == 1:
                    dp[i] = max(nums[0], nums[1])
                else:
                    dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]
