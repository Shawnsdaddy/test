from tree_node import TreeNode


def trim_b_s_t(root: TreeNode, minimum: int, maximum: int) -> TreeNode:
    if not root:
        return
    if minimum <= root.val <= maximum:
        if root.left:
            root.left = trim_b_s_t(root.left, minimum, maximum)
        if root.right:
            root.right = trim_b_s_t(root.right, minimum, maximum)
        return root
    elif root.val < minimum:
        if root.right:
            return trim_b_s_t(root.right, minimum, maximum)
    else:
        if root.left:
            return trim_b_s_t(root.left, minimum, maximum)





