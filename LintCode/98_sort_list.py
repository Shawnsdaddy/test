from tree_node import ListNode


def sort_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    mid = find_middle_node(head)
    mid_next = mid.next
    mid.next = None

    sorted_left = sort_list(head)
    sorted_right = sort_list(mid_next)
    return merge_list(sorted_left, sorted_right)


def merge_list(left: ListNode, right: ListNode):
    head = ListNode(float('-inf'))
    cur = head
    while left and right:
        if left.val > right.val:
            cur.next = right
            cur = cur.next
            right = right.next
        else:
            cur.next = left
            cur = cur.next
            left = left.next
    if left:
        cur.next = left
    if right:
        cur.next = right
    return head.next


def find_middle_node(node: ListNode) -> ListNode:
    if node:
        middle = node
        current = node
        while current.next and current.next.next:
            middle = middle.next
            current = current.next.next
        return middle
    else:
        return None

head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)

# 对链表进行归并排序
sorted_head = sort_list(head)

# 打印排序后的链表
while sorted_head:
    print(sorted_head.val, end=" -> ")
    sorted_head = sorted_head.next
print("None")