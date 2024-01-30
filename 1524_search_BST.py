from tree_node import TreeNode


def search_b_s_t(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return None
    stack = [root]
    while len(stack)>0:
        cur = stack.pop()
        if val == cur.val:
            return cur
        elif val> cur.val:
            if cur.right:
                stack.append(cur.right)
        else:
            if cur.left:
                stack.append(cur.left)