# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    depth_dict = {}

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True
        else:
            left_depth = self.depth(root.left)
            right_depth = self.depth(root.right)
            return (abs(left_depth - right_depth) < 2) and self.isBalanced(root.right) and self.isBalanced(root.left)

    def depth(self, node):
        if node in self.depth_dict:
            return self.depth_dict[node]
        elif node is None:
            return 0
        else:
            self.depth_dict[node] = 1 + max(self.depth(node.right), self.depth(node.left))
            return self.depth_dict[node]
