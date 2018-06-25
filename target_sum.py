class Solution:
    def __init__(self):
        self.cache = {}
        self.count = 0

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.sub_find(0, nums, 0, S)

    def sub_find(self, idx, nums, acc, S):
        if (idx, acc) in self.cache:
            return self.cache[(idx, acc)]
        else:
            res = 0
            if idx == len(nums):
                if acc == S:
                    res = 1
            else:
                res = self.sub_find(idx + 1, nums, acc + nums[idx], S) + self.sub_find(idx + 1, nums, acc - nums[idx],
                                                                                       S)
            self.cache[(idx, acc)] = res
            return self.cache[(idx, acc)]
