import sys

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        t_dict = {}
        for c in t:
            if c not in t_dict:
                t_dict[c] = 1
            else:
                t_dict[c] += 1
        for c in s:
            if c not in t_dict:
                t_dict[c] = 0

        start, end, counter = 0, 0, len(t)
        head = 0
        d = sys.maxsize

        while end < len(s):
            if t_dict[s[end]] > 0:
                counter -= 1
                t_dict[s[end]] -= 1

                while counter == 0:
                    if end - start < d:
                        d = end - start + 1
                        head = start

                    if t_dict[s[start]] == 0:
                        counter += 1

                    t_dict[s[start]] += 1
                    start += 1
            else:
                t_dict[s[end]] -= 1
            end += 1

        return "" if d == sys.maxsize else s[head:head + d]

