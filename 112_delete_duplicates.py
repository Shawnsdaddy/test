class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def delete_duplicates(head: ListNode) -> ListNode:
    if head is None:
        return head
    value = [head.val]
    root = ListNode(0,head)
    while head.next is not None:
        if head.next.val in value:
            head = head.next.next
        else:
            head = head.next
    return root.next