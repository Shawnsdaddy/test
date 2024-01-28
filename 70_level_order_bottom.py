from typing import List
from tree_node import TreeNode


def level_order_bottom(root: TreeNode) -> List[List[int]]:
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
            if cur.left:
                stack.insert(0, cur.left)
            if cur.right:
                stack.insert(0, cur.right)
        level_stack = stack
        res.inser(0,value)
    return res
