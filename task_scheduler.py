import heapq


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        n += 1
        ans = 0

        d = collections.Counter(tasks)
        heap = [-c for c in d.values()]

        heapq.heapify(heap)

        while heap:
            stack = []
            cnt = 0
            for _ in range(n):
                if heap:
                    c = heapq.heappop(heap)
                    cnt += 1
                    if c < 0:
                        stack.append(c + 1)

            for item in stack:
                if item < 0:
                    heapq.heappush(heap, item)

            ans += n if heap else cnt

        return ans