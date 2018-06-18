class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        sort_list = sorted(nums1 + nums2)

        length = len(sort_list)

        if (length % 2) == 0:
            return (sort_list[(0 + length - 1) // 2] + sort_list[((0 + length - 1) // 2) + 1]) / 2
        else:
            return sort_list[(0 + length - 1) // 2]
