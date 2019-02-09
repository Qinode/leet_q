class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        if (len(nums) == 0):
            return []
        elif (k == 0):
            return [max(nums)]
        else:            
            max_window = [0] * (len(nums) - k + 1)

            for i in range(len(max_window)):
                max_window[i] = max(nums[i: i+k])

            return max_window
        