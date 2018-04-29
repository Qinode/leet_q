# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return []
        else:
            result = []

            queue = [root]
            while len(queue) != 0:
                node = queue[0]
                del queue[0]
                if node is not None:
                    result.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            return result


