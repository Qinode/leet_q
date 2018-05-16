class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0 or len(nums) == 1 or len(nums) == 2:
            return list(set(nums))
        else:

            candidate1, candidate2, count1, count2 = 0, 0, 0, 0

            for n in nums:
                if count1 == 0 and n != candidate2:
                    candidate1 = n

                if count2 == 0 and n != candidate1:
                    candidate2 = n

                if n == candidate1:
                    count1 += 1

                if n == candidate2:
                    count2 += 1

                if n != candidate1 and n != candidate2:
                    count1 -= 1
                    count2 -= 1

            count1, count2 = 0, 0
            for x in nums:
                if x == candidate1:
                    count1 += 1
                elif x == candidate2:
                    count2 += 1
                else:
                    continue

            res = []
            if count1 > len(nums) // 3:
                res.append(candidate1)

            if count2 > len(nums) // 3:
                res.append(candidate2)

            return res

