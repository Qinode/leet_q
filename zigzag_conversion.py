 class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s
        
        # if row 0, index: col * (2 * numRows -2)
        # if row numRows-1, index: col * (2 * numRows -2) + numRows
        # if row in (0, numRows-1)
        #   1. col * (2 * numRows -2) + rowNum
        #   2. col * (2 * numRows -2) - rowNum, in here col >= 1

        result = ''

        for i in range(numRows):
            if i == 0:
                col = 0
                while (col * (2 * numRows - 2)) < len(s):
                    result += s[col * (2 * numRows - 2)]
                    col += 1
            elif i > 0 and i < numRows - 1:
                col = 0
                while (col * (2 * numRows -2) + i) < len(s):
                    result += s[col * (2 * numRows -2) + i]
                    
                    if ((col + 1) * (2 * numRows -2) - i) < len(s):
                        result += s[(col + 1) * (2 * numRows -2) - i]

                    col += 1
            else:
                col = 0
                while (col * (2 * numRows -2) + numRows - 1) < len(s):
                    result += s[col * (2 * numRows -2) + numRows - 1]
                    col += 1

        return result



           
