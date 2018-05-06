# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        acc = []
        self.backtrack(acc, [], root, sum)
        return acc

    def backtrack(self, acc, l, node, sum):
        if node is None:
            return
        elif sum == node.val and node.left is None and node.right is None:
            acc.append(l[:] + [node.val])
            return
        else:
            l.append(node.val)
            self.backtrack(acc, l, node.left, sum - node.val)
            self.backtrack(acc, l, node.right, sum - node.val)
            l.pop()
