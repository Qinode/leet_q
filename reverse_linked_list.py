# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head, _ = self.sub_reverse_list(head)
        return head

    def sub_reverse_list(self, head):
        if head is None:
            return None, None
        elif head.next is None:
            return head, head
        elif head.next.next is None:
            new_head = head.next
            head.next = None
            new_head.next = head
            return new_head, head
        else:
            rest = head.next
            head.next = None
            new_head, tail = self.sub_reverse_list(rest)
            tail.next = head
            return new_head, head

    def stack_reverse_list(self, head):
        if head is None:
            return None
        else:
            stack = []
            while head is not None:
                stack.append(head)
                head = head.next

            new_head = copy = stack.pop()
            while len(stack) > 0:
                copy.next = stack.pop()
                copy = copy.next
            copy.next = None

            return new_head