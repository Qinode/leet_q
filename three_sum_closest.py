class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        distance = pow(2, 31) - 1
        closest = 0

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                left, right = i + 1, len(nums) - 1
                while right > left:
                    three_sum = nums[i] + nums[left] + nums[right]
                    
                    if three_sum == target:
                        return target

                    elif three_sum > target:
                        if three_sum - target < distance:
                            distance = three_sum - target
                            closest = three_sum
                        while right > left and nums[right] == nums[right-1]:
                            right -= 1
                        right -= 1

                    else:
                        if target - three_sum < distance:
                            distance = target - three_sum
                            closest = three_sum
                        while right > left and nums[left] == nums[left+1]:
                            left += 1
                        left += 1
        return closest
