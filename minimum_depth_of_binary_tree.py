class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            min_depth = float('inf')
            for c in [root.left, root.right]:
                if c:
                    min_depth = min(self.minDepth(c), min_depth)
            return min_depth + 1