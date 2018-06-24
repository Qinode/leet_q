class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is not None:
            return self.equal(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            return False

    def equal(self, t1, t2):
        if t1 is not None and t2 is not None:
            return t1.val == t2.val and self.equal(t1.left, t2.left) and self.equal(t1.right, t2.right)
        elif t1 is None and t2 is None:
            return True
        else:
            return False