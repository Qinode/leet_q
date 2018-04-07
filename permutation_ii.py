class Solution:

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        record = []

        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            for i in range(len(nums)):
                if nums[i] not in record:
                    record.append(nums[i])
                    for res in self.permuteUnique(nums[0:i]+nums[i+1:]):
                        result.append(([nums[i]] + res))
                else:
                    continue
        return result
