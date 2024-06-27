from tree_node import TreeNode

def is_valid_b_s_t(root: TreeNode) -> bool:
    if not root:
        return True
    else:
        lst = helper(root,[])
        if len(lst) ==1:
            return True
        else:
            valid = True
            index = 1
            while valid and index<len(lst):
                valid = lst[index-1]<lst[index]
                index+=1
            return valid

def helper(self, root:TreeNode, lst):
    if not root:
        return lst
    else:
        self.helper(root.left,lst)
        lst.append(root.val)
        self.helper(root.right,lst)
        return lst



