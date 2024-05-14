from tree_node import TreeNode


def fix_b_s_t(root: TreeNode) -> TreeNode:
    first_element = None
    second_element = None
    pre_node = TreeNode(float('-inf'))

    def inorder_traversal(node: TreeNode):
        nonlocal first_element,second_element,pre_node
        if not node:
            return
        inorder_traversal(node.left)
        if first_element is None and pre_node.val > node.val:
            first_element = pre_node
        if first_element is not None and pre_node.val > node.val:
            second_element = node
        pre_node = node
        inorder_traversal(node.right)

    inorder_traversal(root)

    first_element.val, second_element.val = second_element.val, first_element.val



root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)

print("修复前中序遍历:")

def print_inorder(node):
    if not node:
        return
    print_inorder(node.left)
    print(node.val, end=" ")
    print_inorder(node.right)

print_inorder(root)
print()

# 修复BST
fix_b_s_t(root)

print("修复后中序遍历:")
print_inorder(root)
print()