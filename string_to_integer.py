class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        str = str.strip()

        digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        minus = 0
        my_int = ''

        for x in str:
            if x == '-':
                minus += 1
            elif x == '+':
                continue
            elif x in digit:
                my_int += x
            else:
                break

        try:
            int_val  = int(my_int)
        except ValueError:
            int_val = 0

        if (minus % 2) == 0:
            return int_val
        else:
            return -int_val
