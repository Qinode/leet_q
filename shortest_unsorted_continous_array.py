class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sorted_nums = sorted(nums)

        left = 0
        while left < len(nums):
            if sorted_nums[left] == nums[left]:
                left += 1
            else:
                break

        right = len(nums) - 1
        while right > 0:
            if sorted_nums[right] == nums[right]:
                right -= 1
            else:
                break

        if right < left:
            return 0
        else:
            return right - left + 1
