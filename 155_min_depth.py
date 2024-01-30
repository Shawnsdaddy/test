from tree_node import TreeNode


def min_depth(self, root: TreeNode) -> int:
    # write your code here
    if not root:
        return 0
    stack = [root]
    min_depth = -1
    level = 1
    while len(stack)>0 and min_depth==-1:
        level_stack = []
        while len(stack)>0:
            cur = stack.pop()
            if not cur.left and not cur.right:
                min_depth = level
                break
            if cur.left:
                level_stack.append(cur.left)
            if cur.right:
                level_stack.append(cur.right)
        level+=1
        stack.extend(level_stack)
    return min_depth

