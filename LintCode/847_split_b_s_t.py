from tree_node import TreeNode


def split_b_s_t(root: TreeNode, v: int) -> TreeNode:
    pass



def left_bianli(root: TreeNode, v ):
    if root is None:
        return
    # print(root.val)
    if left_bianli(root.left,v) is not None:
        return root
    if root.val > v:
        return root
    if left_bianli(root.right,v) is not None:
        return root








root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
print(left_bianli(root,2).val)
