# Definition for a binary tree node.
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if len(preorder) == 0:
            return None
        else:
            root = TreeNode(preorder[0])
            r_index = inorder.index(preorder[0])
            left_inorder = inorder[:r_index]
            right_inorder = inorder[r_index + 1:]
            root.left = self.buildTree(preorder[1: len(preorder)-len(right_inorder)], left_inorder)
            root.right = self.buildTree(preorder[len(preorder)-len(right_inorder):], right_inorder)
            return root