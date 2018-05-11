# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None or head.next.next is None:
            return head
        else:
            odd = head
            even_head = even = head.next

            while even is not None and even.next is not None:
                next_odd = odd.next.next
                next_even = even.next.next

                odd.next = next_odd
                even.next = next_even

                odd = odd.next
                even = even.next

            odd.next = even_head

            return head

