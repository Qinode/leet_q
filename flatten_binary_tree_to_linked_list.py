# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        if root is None:
            return root
        else:
            self.flatten(root.left)
            self.flatten(root.right)

            if root.left is None:
                return
            else:
                left_child = root.left
                while left_child.right is not None:
                    left_child = left_child.right

                left_child.right = root.right
                root.left, root.right = None, root.left



