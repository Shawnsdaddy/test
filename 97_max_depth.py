class TreeNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.left = None
        self.right = None
def max_depth(self, root: TreeNode, depth=1) -> int:
    # write your code here
    if not root:
        return 0
    left, right = depth, depth
    if root.left:
        left = self.max_depth(root.left, depth + 1)
    if root.right:
        right = self.max_depth(root.right, depth + 1)

    return max(left, right, depth)
