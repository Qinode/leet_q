class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 0 or len(nums) == 1:
            pass
        else:
            idx = 0
            zeros = non_zeros = 0

            while zeros + non_zeros != len(nums):
                if nums[idx] == 0:
                    nums.append(0)
                    del nums[idx]
                    zeros += 1
                else:
                    idx += 1
                    non_zeros += 1
