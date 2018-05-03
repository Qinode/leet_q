# Definition for singly-linked list with a random pointer.

# Python 2.7

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# Definition for singly-linked list with a random pointer.

# Python 2.7


class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if head is None:
            return head
        else:
            copy = RandomListNode(0)
            copy_h = copy

            backward_lookup = {}
            forward_lookup = {}

            while head is not None:

                copy.next = RandomListNode(head.label)
                backward_lookup[head] = copy.next

                if head.random is None:
                    copy.next.random = None
                elif head.random == head:
                    copy.next.random = copy.next
                else:
                    if head.random in backward_lookup:
                        copy.next.random = backward_lookup[head.random]
                    else:
                        if head.random in forward_lookup:
                            forward_lookup[head.random].append(copy.next)
                        else:
                            forward_lookup[head.random] = [copy.next]

                if head in forward_lookup:
                    for node in forward_lookup[head]:
                     node.random = copy.next

                copy = copy.next
                head = head.next

        return copy_h.next

    # def copyRandomList(self, head):
    #     """
    #     :type head: RandomListNode
    #     :rtype: RandomListNode
    #     """
    #     dic = dict()
    #     m = n = head
    #     while m:
    #         dic[m] = RandomListNode(m.label)
    #         m = m.next
    #
    #     while n:
    #         dic[n].next = dic.get(n.next, None)
    #         dic[n].random = dic.get(n.random, None)
    #         n = n.next
    #     return dic.get(head)
