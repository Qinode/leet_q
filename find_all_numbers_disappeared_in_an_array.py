class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        numbers = [1 for _ in range(len(nums))]
        for x in nums:
            if numbers[x - 1] == 1:
                numbers[x - 1] = 0
            else:
                continue

        return [x + 1 for x in range(len(numbers)) if numbers[x] == 1]
