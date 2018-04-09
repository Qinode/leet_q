class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        missing = 1
        while True:
            if missing not in nums:
                return missing
            else:
                missing += 1
        
        return missing
        
