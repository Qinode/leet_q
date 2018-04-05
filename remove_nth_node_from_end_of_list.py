# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        copy = head

        while copy is not None:
            forward_pointer = copy
            for _ in range(n+1):
                try:
                    forward_pointer = forward_pointer.next
                except AttributeError:
                    return head.next

            if forward_pointer is not None:
                copy = copy.next
            else:
                copy.next = copy.next.next
                return head

        # if n == 1:
        #    while copy.next.next is not None:
        #        copy= copy.next
        #    copy.next = None
        #    return head
        # else:
        #     return None

