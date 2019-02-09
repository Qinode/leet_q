class Solution:
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        else:
            height = [0] * len(matrix[0])
            max_rect = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    height[j] = 0 if matrix[i][j] == '0' else height[j] + 1
                    
                max_rect = max(max_rect, self.max_rectangle(height))
                    
            return max_rect
            
    
    def max_rectangle(self, val):
        
        max_rect = 0
        val.append(0)
        stack = []
        for i in range(len(val)):
            while len(stack) > 0 and val[stack[-1]] >= val[i]:
                idx = stack.pop()
                height = val[idx]
                width = i - (stack[-1] if len(stack) > 0 else -1) - 1
                max_rect = max(max_rect, height * width)
            
            stack.append(i)
        del val[-1]
        return max_rect