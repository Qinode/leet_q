class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 10:
            return -1
        else:
            nums = list(str(n))

            i = len(nums) - 1
            while nums[i] <= nums[i - 1] and i > 0:
                i -= 1

            if i == 0:
                return -1
            else:
                pivot = i - 1
                for j in reversed(range(pivot + 1, len(nums))):
                    if nums[j] > nums[pivot]:
                        nums[j], nums[pivot] = nums[pivot], nums[j]
                        break

                nums = nums[:pivot + 1] + nums[pivot + 1:][::-1]
                res = int(''.join([str(n) for n in nums]))
                return -1 if res > (pow(2, 31) - 1) else res

