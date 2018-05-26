class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[y].append(x)

        visited = [0] * numCourses
        res = []

        for n in range(numCourses):
            if visited[n] != 1:
                self.dfs_topo_sort(n, graph, visited, res)

        return res if len(res) == numCourses else []

    def dfs_topo_sort(self, node, graph, visited, res):
        visited[node] = -1
        for n in graph[node]:
            if visited[n] == -1:
                res = []
            if visited[n] == 0:
                self.dfs_topo_sort(n, graph, visited, res)
        visited[node] = 1
        res.insert(0, node)