class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left, right = 0, len(nums) - 1
        mid = (left + right)//2

        if not nums or target > nums[-1] or target < nums[0]:
            return[-1, -1]

        while left <= right:
            if nums[mid] == target:
                left_offset, right_offset = 0, 0

                while mid + right_offset < len(nums) and nums[mid + right_offset] == target:
                    right_offset += 1

                while mid - left_offset >= 0 and nums[mid - left_offset] == target:
                    left_offset += 1

                return [mid - left_offset + 1, mid + right_offset - 1]
            elif nums[mid] > target:
                right = mid - 1
                mid = (left + right)//2
            else:
                left = mid + 1
                mid = (left + right)//2


        return [-1, -1]
