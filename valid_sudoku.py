class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for row in board:
            if self.is_valid(row):
                continue
            else:
                return False

        for i in range(9):
            if self.is_valid([board[j][i] for j in range(9)]):
                continue
            else:
                return False

        for i in range(9):
            row = 3 * (i // 3)
            col = 3 * (i % 3)
            if self.is_valid([board[j][k] for j in range(row, row+3) for k in range(col, col+3)]):
                continue
            else:
                return False

        return True

    def is_valid(self, data):
        tmp = set()
        for d in data: 
            if d != '.' and d in tmp:
                return False
            else:
                tmp.add(d)
        return True


        
