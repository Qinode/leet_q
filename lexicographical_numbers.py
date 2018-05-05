class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        acc = []
        self.backtrack(acc, 1, n)
        return acc

    def backtrack(self, acc, counter, n):
        if counter > n:
            return
        elif len(acc) == n:
            return
        else:
            acc.append(counter)
            self.backtrack(acc, counter * 10, n)
            if counter % 10 != 9:
                self.backtrack(acc, counter + 1, n)


