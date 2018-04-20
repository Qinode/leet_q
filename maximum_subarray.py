class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum = [nums[0] for _ in range(len(nums))]
        maximum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] + sum[i - 1] > sum[i - 1] and sum[i - 1] < 0:  # negative + positive
                sum[i] = nums[i]
            elif sum[i - 1] < 0 and nums[i] <= 0:  # negative + non-positive
                sum[i] = max(sum[i - 1], nums[i])
            else:
                sum[i] = sum[i - 1] + nums[i]  # positive + positive
            maximum = max(maximum, sum[i])

        return maximum
