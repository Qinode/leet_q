import heapq


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        index_map = {}
        freq = []

        for ch in s:
            if ch in index_map:
                freq[index_map[ch]] = (freq[index_map[ch]][0] + 1, freq[index_map[ch]][1])
            else:
                freq.append((1, ch))
                index_map[ch] = len(freq) - 1

        heapq._heapify_max(freq)
        res = ''

        while len(freq) != 0:
            max_ch = heapq._heappop_max(freq)
            res += max_ch[1] * max_ch[0]

        return res
