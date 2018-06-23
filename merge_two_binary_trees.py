class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        elif t1 is None or t2 is None:
            return t1 or t2
        else:
            new_root = TreeNode(t1.val + t2.val)
            new_root.left = self.mergeTrees(t1.left, t2.left)
            new_root.right = self.mergeTrees(t1.right, t2.right)

            return new_root
