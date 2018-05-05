class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        circles = []
        for i in range(len(M)):
            has_circle = False
            for c in circles:
                if i in c:
                    has_circle = True
                    break
                else:
                    continue
            if not has_circle:
                circle = set()
                stack = [i]
                while len(stack) != 0:
                    item = stack.pop()
                    circle.add(item)
                    for j in range(len(M[item])):
                        if j not in circle and M[item][j] == 1:
                            stack.append(j)

                circles.append(circle)

        return len(circles)
