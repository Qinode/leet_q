class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        costs = [0, cost[0]]
        for i in range(1, len(cost)):
            costs.append(min(costs[i + 1 - 2] + cost[i], costs[i + 1 - 1] + cost[i]))

        return min(costs[-1], costs[-2])


