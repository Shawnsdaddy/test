from typing import List
from tree_node import TreeNode, ListNode


def binaryTreeToLists(root: TreeNode) -> List[List[int]]:
    res = []
    if not root:
        return res
    level_stack = []
    level_stack.append(root)
    while len(level_stack) > 0:
        stack = []
        value = []
        while len(level_stack) > 0:
            cur = level_stack.pop()
            value.append(cur.val)
            if cur.right:
                stack.insert(0, cur.right)
            if cur.left:
                stack.insert(0, cur.left)
        level_stack = stack

        if len(value)>0:
            cur = ListNode(value.pop())
            head = ListNode(-1)
            head.next = cur
        while len(value)>0:
            cur.next = ListNode(value.pop())
            cur = cur.next
        res.append(head.next)
    return res