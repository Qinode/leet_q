# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        return self.sub_add_two_numbers(l1, l2)

    def sub_add_two_numbers(self, l1, l2):
        if (l1 is None) and (l2 is not None):
            return l2
        elif (l1 is not None) and (l2 is None):
            return l1
        elif (l1 is None) and (l2 is None):
            return None
        else:
            val = l1.val + l2.val
            if val >= 10:
                val -= 10
                if l1.next is not None:
                    self.increment(l1)
                else:
                    next = ListNode(1)
                    next.next = None
                    l1.next = next
            
            output = ListNode(val)
            output.next = self.sub_add_two_numbers(l1.next, l2.next)

            return output

    def increment(self, l1):
        if l1 is not None:
            l1.val += 1
            if l1.val >= 10:
                l1.val -= 10
                l1.next = increment(l1.next)
        else:
            l1 = ListNode(1)
            l1.next=None

        return l1
        
