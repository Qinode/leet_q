# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.sub_rob(root, {})

    def sub_rob(self, root, dp):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root in dp:
            return dp[root]

        rob_val = 0

        if root is None:
            return 0

        if root.left is not None:
            rob_val += self.sub_rob(root.left.left, dp) + self.sub_rob(root.left.right, dp)

        if root.right is not None:
            rob_val += self.sub_rob(root.right.left, dp) + self.sub_rob(root.right.right, dp)

        dp[root] = max(rob_val + root.val,
                       self.sub_rob(root.left, dp) + self.sub_rob(root.right, dp))  # max(rob root, rob root's child)
        return dp[root]

