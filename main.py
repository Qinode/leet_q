from remove_nth_node_from_end_of_list import Solution, ListNode

if __name__ =='__main__':
    solution = Solution()
    i = [1, 2, 3, 4, 5, 6, 7]
    inode = [ListNode(num) for num in i]

    head = inode[0]
    copy = head
    for i in range(1, len(inode)):
        copy.next = inode[i]
        copy = copy.next

    res = solution.removeNthFromEnd(head, 7)
    while res is not None:
        print(res.val)
        res = res.next
