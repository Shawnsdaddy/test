from tree_node import TreeNode, ListNode


def addTwoNumbers(l1:ListNode,l2:ListNode):
    def get_number(l: ListNode):
        index = 1
        res = 0
        cur = l
        while cur:
            res += index * cur.val
            index *= 10
            cur = cur.next
        return res

    nums1 = get_number(l1)
    nums2 = get_number(l2)
    res = str(nums1 + nums2)
    res = res[::-1]
    dummy = ListNode()
    cur = ListNode()
    dummy.next = cur
    for i in range(len(res)):
        cur.next = ListNode(int(res[i]))
        cur = cur.next
    return dummy.next.next


