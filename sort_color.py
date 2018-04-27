class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        colors = [0, 0, 0]

        for i in nums:
            colors[i] += 1

        index = 0
        for i, n in enumerate(colors):
            counter = 0
            while counter < n:
                nums[index] = i
                counter += 1
                index += 1


