from tree_node import TreeNode


def max_path_sum(root: TreeNode) -> int:
    if not root:
        return 0
    max_left,max_right = 0,0
    if root.left:
        max_left = max_path_sum(root.left)
    if root.right:
        max_right = max_path_sum(root.right)
    return root.val+ max(max_left,max_right)
