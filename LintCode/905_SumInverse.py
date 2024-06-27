def depthSumInverse(nestedList):
    def helper(nestedList):
        has_list = any(isinstance(e, list) for e in nestedList)
        if not has_list:
            total = 0
            for e in nestedList:
                total += e
            return 1, total
        else:
            curr_level = 1
            existing = 0
            for e in nestedList:
                if isinstance(e, list):
                    res = helper(e)
                    if res[0] > curr_level:
                        curr_level = res[0]
                    existing += res[1]
            total = 0
            for e in nestedList:
                if not isinstance(e, list):
                    total += e
            return curr_level + 1, total * (curr_level + 1) + existing

    l, s = helper(nestedList)
    return s


print(depthSumInverse([[1, 1], 2, [1, 1]]))
