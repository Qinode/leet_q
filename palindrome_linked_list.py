# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        copy = head

        forward = []
        while head is not None:
            forward.append(head.val)
            head = head.next

        idx = len(forward) - 1
        while copy is not None:
            if forward[idx] == copy.val:
                copy = copy.next
                idx -= 1
            else:
                return False

        return True

