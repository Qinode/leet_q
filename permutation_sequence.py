class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = [1 for _ in range(10)]
        for i in range(1, 10):
            factorial[i] = factorial[i - 1] * i

        nums = [i for i in range(1, n + 1)]

        res = []
        k -= 1

        for i in range(1, n + 1):
            index = k // factorial[n - i]
            res.append(nums[index])
            del nums[index]
            k -= index * factorial[n - i]

        return ''.join([str(n) for n in res])