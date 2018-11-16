# Definition for a binary tree node.
# class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '*'
        else:
            serial_root = ''
            queue = [root]

            while len(queue) != 0:
                head = queue[0]
                del queue[0]

                if head:
                    serial_root += '{},'.format(head.val)
                    queue.append(head.left)
                    queue.append(head.right)
                else:
                    serial_root += '*,'
            return serial_root[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data[0] == '*':
            return None
        else:
            nodes = []

            start, end = 0, 0
            while end < len(data):
                while end < len(data) and data[end] != ',':
                    end += 1

                val = data[start:end]
                start = end = end + 1

                if val != '*':
                    node = TreeNode(int(val))
                    nodes.append(node)
                else:
                    nodes.append(None)

            next = [1, 2]
            for i in range(len(nodes)):
                if nodes[i]:
                    if next[0] < len(nodes):
                        nodes[i].left = nodes[next[0]]
                        next[0] += 2

                    if next[1] < len(nodes):
                        nodes[i].right = nodes[next[1]]
                        next[1] += 2

            return nodes[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))