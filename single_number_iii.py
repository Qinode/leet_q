class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        xor = 0
        for num in nums:
            xor ^= num

        last_set_bit = xor & (-xor)

        res = [0, 0]
        for num in nums:
            if (num & last_set_bit) == 0:
                res[0] ^= num
            else:
                res[1] ^= num

        return res