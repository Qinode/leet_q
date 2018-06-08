class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sm = sum(nums)

        if sm % 2: return False

        half = sm // 2

        #  All possible sum from the array are computed and
        # cached in the set
        curr = set([0])
        for n in nums:
            curr.update([nn + n for nn in curr])
            if half in curr: return True

        return False