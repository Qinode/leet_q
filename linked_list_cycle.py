# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        tortorise = hare = head
        while hare is not None and hare.next is not None:
            tortorise = tortorise.next
            hare = hare.next.next
            if hare == tortorise:
                return True

        return False