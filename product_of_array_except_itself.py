class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        forward_prod = [1]
        for n in nums:
            forward_prod.append(n * forward_prod[-1])
        forward_prod = forward_prod[1:]

        backward_prod = [1]
        for n in reversed(nums):
            backward_prod.insert(0, n * backward_prod[0])
        backward_prod = backward_prod[:-1]

        res = [1 for _ in range(len(nums))]
        res[0] = backward_prod[1]
        res[-1] = forward_prod[-2]

        for i in range(1, len(nums) - 1):
            res[i] = forward_prod[i - 1] * backward_prod[i + 1]

        return res



