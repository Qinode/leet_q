class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []
        candidates.sort()
        self.sub_combination_sum(result, [], candidates, target, 0)
        return result

    def sub_combination_sum(self, list, acc, candidates, target, start):
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            else:
                if candidates[i] > target:
                    return
                elif candidates[i] == target:
                    ans = acc[:]
                    ans.append(candidates[i])
                    list.append(ans)
                else:
                    sub_target = target - candidates[i]
                    acc.append(candidates[i])
                    self.sub_combination_sum(list, acc, candidates, sub_target, i+1)
                    acc.remove(candidates[i])