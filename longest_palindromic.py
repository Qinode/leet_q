class Solution(object): 
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Maximum size of s is 1000

        if len(s) == 0:
            return ""

        size = len(s)
        longest_size = 1
        start = 0

        for i in range(size):
            if (i - longest_size) >= 1 and s[i-longest_size-1:i+1] == s[i-longest_size-1:i+1][::-1]:
                start = i-longest_size - 1
                longest_size += 2
                continue

            if (i - longest_size) >= 0 and s[i-longest_size:i+1] == s[i-longest_size:i+1][::-1]:
                start = i - longest_size
                longest_size += 1

        return s[start:start+longest_size]
