class Solution:

    def __init__(self):
        self.len = 0
        self.ans = set()

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        self.len = len(s.replace('(', '').replace(')', ''))
        self.sub_removing([], s, 0, 0)
        return list(self.ans)

    def sub_removing(self, exp, string, left, right):

        if left == right and len(exp) > self.len:
            self.ans.clear()
            self.len = len(exp)
            self.ans.add(''.join(exp))

        if left == right and len(exp) == self.len:
            self.ans.add(''.join(exp))

        if string == "":
            return

        if string[0] == '(':
            self.sub_removing(exp + ['('], string[1:], left + 1, right)
            self.sub_removing(exp, string[1:], left, right)
        elif string[0] == ')':
            if left - right > 0:
                self.sub_removing(exp + [')'], string[1:], left, right + 1)
                self.sub_removing(exp, string[1:], left, right)
            else:
                self.sub_removing(exp, string[1:], left, right)
        else:
            self.sub_removing(exp + [string[0]], string[1:], left, right)
