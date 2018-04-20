class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        maximum = [nums[0] for _ in range(len(nums))]
        minimum = [nums[0] for _ in range(len(nums))]

        for i in range(1, len(nums)):
            maximum[i] = max([nums[i], nums[i] * maximum[i - 1], nums[i] * minimum[i - 1]])
            minimum[i] = min([nums[i], nums[i] * maximum[i - 1], nums[i] * minimum[i - 1]])
            result = max(result, maximum[i])

        return result
