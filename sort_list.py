# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head
        else:
            middle = self.find_middle(head)
            right = middle.next
            middle.next = None
            return self.merge_sort(self.sortList(head), self.sortList(right))

    def find_middle(self, linked_list):
        fast, slow = linked_list, linked_list
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge_sort(self, l1, l2):
        h = h_copy = ListNode(None)
        while l1 is not None and l2 is not None:
            if l1.val >= l2.val:
                h_copy.next = l2
                l2 = l2.next
            else:
                h_copy.next = l1
                l1 = l1.next
            h_copy = h_copy.next

        h_copy.next = l1 or l2
        return h.next
