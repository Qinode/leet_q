class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        heights.append(0)
        stack = []
        r = 0

        for i in range(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = i - (stack[-1] if len(stack) > 0 else -1) - 1
                r = max(r, h * w)

            stack.append(i)

        return r
