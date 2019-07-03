class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []

        if len(matrix) == 1:
            return matrix[0]

        i, j, result = 0, -1, []
        row, col = len(matrix), len(matrix[0])
        visited = [[False for i in range(col)] for i in range(row)]
        direction = 'right'

        while len(result) != row * col:
            if direction == 'right':
                if j + 1 < col and not visited[i][j + 1]:
                    j += 1
                    visited[i][j] = True
                    result.append(matrix[i][j])
                else:
                    direction = 'down'

            if direction == 'down':
                if i + 1 < row and not visited[i + 1][j]:
                    i += 1
                    visited[i][j] = True
                    result.append(matrix[i][j])
                else:
                    direction = 'left'

            if direction == 'left':
                if j - 1 >= 0 and not visited[i][j - 1]:
                    j -= 1
                    visited[i][j] = True
                    result.append(matrix[i][j])
                else:
                    direction = 'up'

            if direction == 'up':
                if i - 1 >= 0 and not visited[i - 1][j]:
                    i -= 1
                    visited[i][j] = True
                    result.append(matrix[i][j])
                else:
                    direction = 'right'
        return result