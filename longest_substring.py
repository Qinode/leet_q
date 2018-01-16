class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_str = len(s)
        longest_len = 0

        for i in range(0, len_str):
            visited = {}
            temp_str = ''
            for j in range(i, len_str):
                if s[j] not in visited:
                    visited[s[j]] = True
                    temp_str += s[j]
                else:
                    break

            if len(temp_str) > longest_len:
                longest_len = len(temp_str)
            else:
                continue

        return longest_len

