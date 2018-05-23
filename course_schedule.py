class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0:
            return True

        graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[y].append(x)

        visited = [0] * numCourses

        for c in range(numCourses):
            if not visited[c]:
                if self.is_cyclic(c, graph, visited):
                    return False

        return True

    def is_cyclic(self, node, graph, visited):
        if visited[node] == -1:
            return True

        if visited[node] == 1:
            return False

        visited[node] = -1
        for n in graph[node]:
            if visited[n] != 1:
                if self.is_cyclic(n, graph, visited):
                    return True

        visited[node] = 1
        return False

    def has_path(self, node1, node2, graph, visited):
        if node1 not in graph:
            return False
        elif node2 in graph[node1]:
            return True
        else:
            next = graph[node1]
            for n in next:
                if n not in visited and self.has_path(n, node2, graph, visited + [n]):
                    return True

            return False
