class Solution(object): 
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Maximum size of s is 1000

        if len(s) == 1:
            return s
        
        if len(s) == 0:
            return ""

        size = len(s)

        longest_palindrome = s[0] 
        longest_size = 1

        for i in range(1, size):
            len_odd, str_odd = self.expand_odd(i, s)
            len_even, str_even = self.expand_even(i, s)

            max_len = max(len_odd, len_even)
            if max_len > longest_size:
                longest_size = max_len
                if len_odd > len_even:
                    longest_palindrome = str_odd
                else:
                    longest_palindrome = str_even

        return longest_palindrome

    def expand_odd(self, pivot, s):
        i = 0
        j = 0

        while (pivot - i) >= 0 and (pivot + j) < len(s):
            if s[pivot - i] == s[pivot + j]:
                i += 1
                j += 1

        return i + j + 1, s[pivot-i:pivot+j+1]

    def expand_even(self,pivot, s):
        i = 0
        j = 0

        if s[pivot] == s[pivot - 1]:
            i += 1
            while (pivot - i)>=0 and (pivot + j) < len(s):
                if s[pivot - i] == s[pivot + j]:
                    i += 1
                    j += 1

        return i + j + 1, s[pivot-i:pivot+j+1]

