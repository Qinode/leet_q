class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_letter = ['I', 'V', 'X', 'L', 'C', 'D', 'M'] 

        str_num = str(num)
        r_str_num = str_num[::-1]
        num = [int(x) for x in str_num]

        roman_integer = []

        for idx, val in enumerate(num):
            if val == 0:
                continue
            elif val < 4:
                roman_integer.append(roman_letter[2 * idx] * val)
            elif val == 4:
                roman_integer.append(roman_letter[2 * idx]  + roman_letter[2 * idx + 1])
            elif val < 9:
                roman_integer.append(roman_letter[2 * idx + 1] + roman_letter[2 * idx] * (val -5))
            elif val == 9:
                roman_integer.append(roman_letter[2 * idx] + roman_letter[2 * idx + 2])

        return ''.join(roman_integer[::-1])
