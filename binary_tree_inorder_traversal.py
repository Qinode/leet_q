# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []
        self.traverse(result, root)
        return result

    def traverse(self, result, root):
        if root == None:
            return
        else:
            self.traverse(result, root.left)
            result.append(root.val)
            self.traverse(result, root.right)

