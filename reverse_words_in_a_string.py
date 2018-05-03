class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        words[:] = [w.strip() for w in reversed(words) if w.strip() != '']
        return ' '.join(words)
