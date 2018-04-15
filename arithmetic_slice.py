class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        else:
            res = 0
            dp = [[(False, 0) for _ in range(len(A))] for _ in range(len(A))]
            for i in range(len(A)):
                for j in range(i + 2, len(A)):
                    if j - i == 2:
                        if A[j] - A[j - 1] == A[j - 1] - A[j - 2]:
                            dp[i][j] = (True, A[j] - A[j - 1])
                            res += 1
                    else:
                        is_slice, slice = dp[i][j - 1]
                        if is_slice and A[j] - A[j - 1] == slice:
                            dp[i][j] = (True, slice)
                            res += 1
                        else:
                            break

        return res
