class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        while '[' in s:
            digit_pos, digit_end = self.find_first_number(s)
            closing = self.find_closing(s[digit_end:]) + digit_end
            if closing != len(s):
                s = s[0:digit_pos] + (int(s[digit_pos: digit_end]) * s[digit_end + 1:closing]) + s[closing + 1:]
            else:
                s = s[0:digit_pos] + (int(s[digit_pos: digit_end]) * s[digit_end + 1:closing])
        return s

    def find_closing(self, s):
        open = 0
        for i in range(1, len(s)):
            if s[i] == '[':
                open += 1
            elif s[i] == ']' and open == 0:
                return i
            elif s[i] == ']' and open > 0:
                open -= 1
            else:
                continue
        return -1

    def find_first_number(self, s):
        start = -1
        end = -1
        for i in range(len(s)):
            if s[i].isdigit():
                start = end = i
                break

        while s[end].isdigit():
            end += 1

        return start, end

