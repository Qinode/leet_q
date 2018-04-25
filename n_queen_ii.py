import copy

class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        board = [['.' for _ in range(n)] for _ in range(n)]
        acc = []
        self.backtracking(acc, board, 0, n)

        result = []
        for ans_board in acc:
            str_board = []
            for row in ans_board:
                str_board.append(''.join(row))
            result.append(str_board)

        return len(result)

    def valid_board(self, board, x, y):

        for i in range(x):
            if board[i][y] == 'Q':
                return False

        for i, j in zip(reversed(range(x)), reversed(range(y))):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(reversed(range(x)), range(y + 1, len(board))):
            if board[i][j] == 'Q':
                return False

        return True

    def backtracking(self, acc, board, row, n):

        if row == n:
            acc.append(copy.deepcopy(board))
            return
        else:
            for j in range(n):
                if self.valid_board(board, row, j):
                    board[row][j] = 'Q'
                    self.backtracking(acc, board, row + 1, n)
                    board[row][j] = '.'
                else:
                    continue

            return