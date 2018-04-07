class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            for i in range(len(nums)):
                for res in self.permute(nums[0:i]+nums[i+1:]):
                    result.append(([nums[i]] + res))
        return result

