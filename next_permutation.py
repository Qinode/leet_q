class Solution:

    def nextPermutation(self, arr):
        """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """

        # Find non-increasing suffix
        i = len(arr) - 1
        while i > 0 and arr[i - 1] >= arr[i]:
            i -= 1
        if i <= 0:
            return None

        # Find successor to pivot
        j = len(arr) - 1
        while arr[j] <= arr[i - 1]:
            j -= 1
        arr[i-1], arr[j] = arr[j], arr[i - 1]

        # Reverse suffix
        arr[i:] = arr[len(arr) - 1:i - 1: -1]
        return None