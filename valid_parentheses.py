class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for ch in s:
            if ch == '[' or ch == '{' or ch == '(':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if self.get_closing(top) == ch:
                    continue
                else:
                    return False
        return len(stack) == 0

    def get_closing(self, ch):
        if ch == '(':
            return ')'
        elif ch == '{':
            return '}'
        else:
            return ']'