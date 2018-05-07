class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        islands = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0':
                    continue

                is_island = False
                for island in islands:
                    if (i, j) in island:
                        is_island = True
                        break
                    else:
                        continue

                if is_island == False:
                    island = set()
                    stack = [(i, j)]
                    while len(stack) != 0:
                        x, y = stack.pop()
                        island.add((x, y))
                        adjacence = self.get_adjacence(x, y, grid)
                        for pos in adjacence:
                            if pos not in island:
                                stack.append(pos)

                    islands.append(island)

        return len(islands)


    def get_adjacence(self, x, y, grid):
        res = []
        for pos in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if pos[0] < 0 or pos[0] == len(grid) or pos[1] < 0 or pos[1] == len(grid[pos[0]]):
                continue
            elif grid[pos[0]][pos[1]] == '0':
                continue
            else:
                res.append(pos)
        return res
