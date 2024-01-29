from tree_node import TreeNode

def insertNode(root, node):
    if not root:
        return TreeNode(node.val)
    else:
        print(root.val)
        if node.val > root.val:
            root.right = insertNode(root.right, node)
        else:
            root.left = insertNode(root.left, node)
        return root

