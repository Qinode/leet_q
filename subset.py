class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return [[]]
        else:
            sub_result = self.subsets(nums[1:])
            result = [[nums[0]] + r for r in sub_result]
            return result + sub_result



