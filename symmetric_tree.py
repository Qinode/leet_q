# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True
        else:
            self.reverse_tree(root.left)
            return self.equal(root.left, root.right)

    def reverse_tree(self, root):
        if root is None:
            return
        else:
            root.right, root.left = root.left, root.right
            self.reverse_tree(root.left)
            self.reverse_tree(root.right)

    def equal(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        else:
            return root1.val == root2.val and self.equal(root1.left, root2.left) and self.equal(root1.right,
                                                                                                root2.right)