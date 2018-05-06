# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # implementation of hare and tortoise algorithm

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        else:
            intersection = self.get_intersection(head)
            if intersection is None:
                return None
            else:
                while head != intersection:
                    head = head.next
                    intersection = intersection.next

                return head

    def get_intersection(self, head):
        tortoise = hare = head
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                return hare

        return None