# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return self.d_search(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def d_search(self, root, sum):
        if root is None:
            return 0
        else:
            count = 0
            if root.val == sum:
                count += 1
            count += self.d_search(root.left, sum - root.val)
            count += self.d_search(root.right, sum - root.val)
            return count




