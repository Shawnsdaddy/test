import math

from tree_node import TreeNode

is_balance = True

def is_balanced(self, root: TreeNode) -> bool:
    # write your code here
    self.helper(root)
    return self.is_balance


def helper(self, root: TreeNode):
    if not self.is_balance:
        return math.inf
    if not root:
        return 0
    left_level = self.helper(root.left) + 1
    right_level = self.helper(root.right) + 1
    if abs(left_level - right_level) >= 2:
        self.is_balance = False
    return max(left_level, right_level)