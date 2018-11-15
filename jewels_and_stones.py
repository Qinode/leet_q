class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        J = set(J)
        js = 0

        for s in S:
            js += 1 if s in J else 0

        return js
