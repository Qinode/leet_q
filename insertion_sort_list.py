# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else:
            tail = head
            copy = head.next
            while copy is not None:
                if copy.val < tail.val:
                    next = copy.next
                    head = self.insert(head, copy)
                    tail.next = next
                    copy = next
                else:
                    tail = tail.next
                    copy = copy.next

            return head

    def insert(self, head, new_node):
        if head is None:
            return new_node
        else:
            if new_node.val < head.val:
                new_node.next = head
                return new_node
            else:
                head.next = self.insert(head.next, new_node)
                return head

