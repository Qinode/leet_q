from min_cost_climbing_stairs import Solution

if __name__ == '__main__':
    solution = Solution()

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]

    r = solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    # r = solution.minCostClimbingStairs([10, 15, 20])
    print(r)
    # print(solution.get_moves(board, 0, 0))

