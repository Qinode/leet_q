class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if len(word) == 0:
            return True
        else:
            coordinate = [(x, y) for x in range(len(board)) for y in range(len(board[x])) if board[x][y] == word[0]]
            if len(coordinate) == 0:
                return False
            else:
                for (x, y) in coordinate:
                    if self.find(board, x, y, word[1:], [(x, y)]):
                        return True
        return False

    def find(self, board, x, y, string, visited):
        if len(string) == 0:
            return True

        moves = self.get_moves(board, x, y)

        for (nx, ny) in moves:
            if board[nx][ny] == string[0] and (nx, ny) not in visited:
                visited.append((nx, ny))
                if self.find(board, nx, ny, string[1:], visited):
                    return True
                visited.remove((nx, ny))

        return False

    def get_moves(self, board, x, y):
        moves = [(new_x, new_y) for new_x in [x, x + 1, x - 1] for new_y in [y, y + 1, y - 1]]
        moves = [(mx, my) for (mx, my) in moves if
                 (mx, my) not in [(x, y), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]]
        if x == 0:
            moves = [(mx, my) for (mx, my) in moves if mx != x - 1]

        if x == len(board) - 1:
            moves = [(mx, my) for (mx, my) in moves if mx != x + 1]

        if y == 0:
            moves = [(mx, my) for (mx, my) in moves if my != y - 1]

        if y == len(board[0]) - 1:
            moves = [(mx, my) for (mx, my) in moves if my != y + 1]

        return moves
