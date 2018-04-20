from triangle import Solution

if __name__ == '__main__':
    solution = Solution()

    path = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]

    r = solution.minimumTotal(path)
    print(r)
