from tree_node import ListNode


def removeNthFromEnd(head:ListNode,k):
    slow = head
    fast = head
    n = 0
    l = 0
    while slow and fast and fast.next:
        slow = slow.next
        n += 1
        fast = fast.next.next
    if fast is not None:
        l = 2 * n + 1
    else:
        l = 2 * n
    index = l - k
    cur = head
    while index > 1:
        cur = cur.next
        index -= 1
    if cur.next and index != 0:
        cur.next = cur.next.next
    if index == 0:
        return head.next
    else:
        return head

head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

removeNthFromEnd(head,2)



