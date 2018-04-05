class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        look_up_table = {
                '0' : ['0'],
                '1' : ['1'],
                '2' : ['a', 'b', 'c'],
                '3' : ['d', 'e', 'f'],
                '4' : ['g', 'h', 'i'],
                '5' : ['j', 'k', 'l'],
                '6' : ['m', 'n', 'o'],
                '7' : ['p', 'q', 'r', 's'],
                '8' : ['t', 'u', 'v'],
                '9' : ['w', 'x', 'y', 'z']
        }

        result = []
        for l in digits:
            if len(result) == 0:
                result = look_up_table[l]
            else:
                tmp = result
                result = [t+letter for t in tmp for letter in look_up_table[l]]

        return result

