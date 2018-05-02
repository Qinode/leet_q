# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r_l1 = self.reverse_linked_list(l1)
        r_l2 = self.reverse_linked_list(l2)

        r_ans = self.add_two_number(r_l1, r_l2)

        return self.reverse_linked_list(r_ans)

    def increment(self, head):
        if head is None:
            return ListNode(1)
        else:
            head.val += 1
            if head.val >= 10:
                head.val -= 10
                head.next = self.increment(head.next)
            return head

    def add_two_number(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            val = l1.val + l2.val
            if val >= 10:
                val -= 10
                l1.next = self.increment(l1.next)

            node = ListNode(val)
            node.next = self.add_two_number(l1.next, l2.next)
            return node

    def reverse_linked_list(self, l):
        if l is None or l.next is None:
            return ListNode(l.val)
        else:
            tail = self.reverse_linked_list(l.next)
            copy = tail
            while copy.next is not None:
                copy = copy.next
            copy.next = ListNode(l.val)
            return tail

