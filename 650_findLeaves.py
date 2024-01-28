from tree_node import TreeNode

def findLeaves(root: TreeNode):
    res = []
    if not root:
        return res
    dfs(root,res)
    return res

def dfs(root:TreeNode,lst):
    if not root:
        return -1
    left_level = dfs(root.left, lst) + 1
    right_level = dfs(root.right, lst) + 1
    cur_level = max(left_level, right_level)
    print(cur_level, left_level, right_level)
    add_to_result(cur_level, root.val, lst)
    return cur_level

def add_to_result(cur_level,val,lst):
    while len(lst) <= cur_level:
        lst.append([])
    lst[cur_level].append(val)

