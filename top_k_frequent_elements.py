import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        c = Counter(nums)

        heap = []
        for key, value in c.items():
            heapq.heappush(heap, (-value, key))

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res