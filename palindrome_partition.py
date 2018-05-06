class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        if s == '':
            return []
        else:
            acc = []
            self.backtrack(acc, [], s)
            return acc

    def backtrack(self, acc, l, s):
        if s == '':
            acc.append(l[:])
        else:
            for i in range(len(s) + 1):
                if s[:i] == s[:i][::-1] and s[:i] != '':
                    l.append(s[:i])
                    self.backtrack(acc, l, s[i:])
                    l.pop()
                else:
                    continue
            return

