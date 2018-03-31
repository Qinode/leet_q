class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                for j in range(i+1, len(nums)):
                    if nums[j] + nums[i] == target:
                        return [i, j]
                    else:
                        continue
        return []



