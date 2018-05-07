class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if len(grid) == 0:
            return 0
        else:
            start = self.find_start(grid)
            if start is None:
                return 0
            else:
                perimeter = 0
                stack = [start]
                visited = set()
                while len(stack) != 0:
                    item = stack.pop()
                    if item not in visited:
                        visited.add(item)
                        adjacent = self.get_adjacence(item[0], item[1], grid)
                        perimeter += 4 - len(adjacent)
                        for p in adjacent:
                            if p not in visited:
                                stack.append(p)

                return perimeter

    def find_start(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return i, j
        return None

    def get_adjacence(self, x, y, grid):
        res = []
        for pos in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if pos[0] < 0 or pos[0] == len(grid) or pos[1] < 0 or pos[1] == len(grid[pos[0]]):
                continue
            elif grid[pos[0]][pos[1]] == 0:
                continue
            else:
                res.append(pos)
        return res






