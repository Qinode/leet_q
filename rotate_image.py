class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """


        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j], matrix[j][j] = matrix[j][j], matrix[i][j]

        for row in range(len(matrix)):
            for i in range(len(row)//2):
                row[i], row[-i-1] = row[-i-1], row[i]



