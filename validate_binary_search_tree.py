# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        array = []
        self.is_valid(root, array)

        for i in range(len(array) - 1):
            if array[i] >= array[i + 1]:
                return False

        return True


    def is_valid(self, root, array):
        if root is not None:
            self.is_valid(root.left, array)
            array.append(root.val)
            self.is_valid(root.right, array)
        else:
            return True

