class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []

        self.backtrack(result, '', 0, 0, n)

        return result
    
    def backtrack(self, result,  s, num_open, num_close, n):
        if len(s) == 2 * n:
            result.append(s)
            return None
        else:
            if num_open < n:
                self.backtrack(self, result, s + '(', num_open + 1, num_ close, n)

            if num_close < num_open:
                self.backtrack(self, result, s + ')', num_open, num_ close + 1, n)

