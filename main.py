from merge_k_sorted_list import ListNode, Compared_Solution

if __name__ =='__main__':
    solution = Compared_Solution()
    i = [1]
    inode = [ListNode(num) for num in i]

    l1 = inode[0]
    copy =l1
    for i in range(1, len(inode)):
        copy.next = inode[i]
        copy = copy.next

    i = [0, 2, 5]
    inode = [ListNode(num) for num in i]

    l2 = inode[0]
    copy =l2
    for i in range(1, len(inode)):
        copy.next = inode[i]
        copy = copy.next

    i = [-2, -1, 0, 2]
    inode = [ListNode(num) for num in i]

    l3 = inode[0]
    copy =l3
    for i in range(1, len(inode)):
        copy.next = inode[i]
        copy = copy.next
    res = solution.mergeKLists([l2])
    while res is not None:
        print(res.val)
        res = res.next
