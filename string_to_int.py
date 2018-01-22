class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        str = str.strip()

        digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        minus = 0
        plus = 0
        my_int = ''

        for x in str:
            if x == '-':
                minus += 1
            elif x == '+':
                plus += 1
            elif x in digit:
                my_int += x
            else:
                break

        if my_int == '' or minus + plus > 1:
            return 0
        elif minus == 1:    # negative number
            if (my_int > '2147483648' and len(my_int) == len('2147483648')) or (len(my_int) > len('2147483648')):
                return -2147483648
            else:
                return - int(my_int)
        else:   # positive number
            if (my_int > '2147483647' and len(my_int)) == len('2147483647') or (len(my_int) > len('2147483648')):
                return 2147483647
            else:
                return int(my_int)
