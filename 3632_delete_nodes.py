from tree_node import ListNode


def delete_nodes(head: ListNode, m: int, n: int) -> ListNode:
    # --- write your code here ---
    def keep_node(current, keep_index):
        while keep_index > 0 and current:
            current = current.next
            keep_index -= 1
        return current

    cur = head
    while cur:
        cur = keep_node(cur, m - 1)
        if cur:
            cur_next = cur.next
            cur.next = None
            cur.next = keep_node(cur_next, n)
        if cur:
            cur = cur.next
    return head
