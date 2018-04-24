class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        position = [i for i in range(n)]
        board = [['.' for _ in range(n)] for _ in range(n)]
        acc = []
        self.backtracking(acc, board, position)
        return acc

    def valid_board(self, board):

        return True

    def backtracking(self, acc, board, position):
        if self.valid_board(board):
            if len(position) == 0:
                acc.append(board)
                return
            else:
                for index, pos in enumerate(position):
                    board[len(board) - len(position)][position[index]] = 'Q'
                    self.backtracking(board, (position[0:index] + position[index + 1:]))
                    board[len(board) - len(position)][position[index]] = '.'
        else:
            return
