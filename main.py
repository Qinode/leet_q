from word_search import Solution

if __name__ == '__main__':
    solution = Solution()

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    board = [['a', 'b'], ['c', 'd']]

    r = solution.exist(board, "abcd")
    print(r)
    # print(solution.get_moves(board, 0, 0))

