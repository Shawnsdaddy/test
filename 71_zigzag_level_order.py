from typing import List


class TreeNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.left = None
        self.right = None

def zigzag_level_order(root: TreeNode) -> List[List[int]]:
    res = []
    if not root:
        return res
    level_stack = []
    left_to_right = True
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
        if not left_to_right:
            value.reverse()
        left_to_right = not left_to_right
        level_stack = stack
        res.append(value)
    return res





