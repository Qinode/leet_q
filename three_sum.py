class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        if len(nums) < 3:
            return result

        nums.sort()
        num_set = set()

        for i in range(1, len(nums) - 1):
            left, right = 0, len(nums) - 1

            while right > left:
                if 0 > nums[i] + nums[left] + nums[right]:
                    left += 1 if left != i-1 else 2
                elif 0 < nums[i] + nums[left] + nums[right]:
                    right -= 1 if right != i+1 else 2
                elif 0 == nums[i] + nums[left] + nums[right]:
                    num_list = [nums[i], nums[left], nums[right]]
                    num_list.sort()
                    num_str = ''.join(str(e) for e in num_list)
                    if num_str not in num_set:
                        num_set.add(num_str)
                        result.append([nums[left], nums[i], nums[right]])
                        right -= 1 if right != i+1 else 2
                    else:
                        right -= 1 if right != i+1 else 2
        return result
