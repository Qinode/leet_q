# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        stack = []
        counter = 0
        while len(stack) != 0 or root is not None:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                pop_item = stack.pop()
                counter += 1
                if counter == k:
                    return pop_item.val
                root = pop_item.right

