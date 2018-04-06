# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Divide and Conquer Solution
class DC_Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next

# Compare by one solution, exceeds time limit
class Compared_Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        heads = []
        for node in lists:
            if node is not None:
                heads.append(node)

        head = copy = ListNode(None)
        while len(heads) != 0:
            min_index = self.find_min(heads)

            copy.next = ListNode(heads[min_index].val)
            copy = copy.next

            if heads[min_index].next is None:
                del heads[min_index]
            else:
                heads[min_index] = heads[min_index].next

        return head.next

    def find_min(self, lists):
        index = 0

        for i in range(1, len(lists)):
            if lists[i].val < lists[index].val:
                index = i
            else:
                continue

        return index
