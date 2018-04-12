class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        result = []
        self.sub_combine(result, [], range(1, n+1), k, 0)
        return result

    def sub_combine(self, result, acc, n, k, start):
        if len(acc) == k:
            tmp = acc[:]
            result.append(tmp)
            return
        else:
            for i in range(start, len(n)):
                acc.append(n[i])
                self.sub_combine(result, acc, n, k, i+1)
                acc.remove(n[i])
