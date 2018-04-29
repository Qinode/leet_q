# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []
        else:
            result = []

            queue = [(root, 0)]
            while len(queue) != 0:
                node, level = queue[0]
                del queue[0]
                if node is not None:
                    if len(result) == level:
                        result.append([node.val])
                    else:
                        if (level + 1) % 2 == 0:
                            result[level].insert(0, node.val)
                        else:
                            result[level].append(node.val)
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))

            return result

