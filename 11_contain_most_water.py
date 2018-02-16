class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        right = len(height) - 1
        left = 0
        max_area = (right - left) * min(height[left], height[right])

        while right - left > 1:
            if min(height[left], height[right]) == height[left]:
                left += 1
                area = (right - left) * min(height[left], height[right])
            elif min(height[left], height[right]) == height[right]:
                right -= 1
                area = (right - left) * min(height[left], height[right])

            if area > max_area:
                max_area = area

        return max_area

        
