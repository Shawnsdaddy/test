from tree_node import TreeNode


def is_subtree(t1: TreeNode, t2: TreeNode) -> bool:
    if not t2:
        return True
    if not t1:
        return False
    if t1.val == t2.val:
        if is_equal(t1.left, t2.left) and is_equal(t1.right, t2.right):
            return True
    return is_subtree(t1.left, t2) or is_subtree(t1.right, t2)

def is_equal(t1: TreeNode, t2: TreeNode) -> bool:
    if t2 is None and t1 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.val == t2.val:
        return is_equal(t1.left, t2.left) and is_equal(t1.right, t2.right)
    else:
        return False

