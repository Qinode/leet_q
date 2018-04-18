from unique_path_ii import Solution

if __name__ == '__main__':
    solution = Solution()

    path = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    r = solution.uniquePathsWithObstacles(path)
    print(r)
