from n_queen import Solution

if __name__ == '__main__':
    solution = Solution()

    path = [10, 9, 2, 5, 3, 4]

    r = solution.solveNQueens(4)
    for i in r:
        print(i)
