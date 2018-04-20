from minimum_path_sum import Solution

if __name__ == '__main__':
    solution = Solution()

    path = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    r = solution.minPathSum(path)
    print(r)
