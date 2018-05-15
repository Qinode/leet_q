class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0:
            return False
        else:
            found = False
            for row in matrix:
                if len(row) != 0:
                    if row[0] <= target:
                        found = self.binary_serach(row, target)
                        if found:
                            return found
                    else:
                        break
            return found

    def binary_serach(self, array, target):
        if len(array) == 0:
            return False
        else:
            start, end = 0, len(array) - 1
            while start <= end:
                middle = (start + end) // 2
                if target == array[middle]:
                    return True
                elif target > array[middle]:
                    start = middle + 1
                else:
                    end = middle - 1
            return False