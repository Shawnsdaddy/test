from tree_node import ListNode


def reverse_list(head:ListNode):
    dummy = ListNode(-1)
    cur = head
    while cur:
        tail = dummy.next
        dummy.next = ListNode(cur.val)
        dummy.next.next = tail
        cur = cur.next
    return dummy.next

def reverseList(head):
    prev_node = None
    current_node = head

    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
reverseList(head)