class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                sub_target = target - nums[i]
                sub_result = self.three_sum(nums[i+1:], sub_target)
                if len(sub_result) != 0:
                    for r in sub_result:
                        r.append(nums[i])
                        result.append(r)
        return result


    def three_sum(self, nums, target):

        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                left, right = i + 1, len(nums) - 1

                while right > left:
                    t_sum = nums[i] + nums[left] + nums[right]
                    if t_sum > target:
                        right -= 1
                    elif t_sum < target:
                        left += 1
                    else:
                        result.append([nums[i], nums[left], nums[right]])
                        while right > left and nums[right] == nums[right-1]:
                            right -= 1
                        while right > left and nums[left] == nums[left+1]:
                            left += 1

                        right -= 1
                        left += 1
        return result