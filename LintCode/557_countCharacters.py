def countCharacters(str):
    # write your code here
    ret = {}
    if str is None or len(str) == 0:
        return ret
    for c in str:
        if c not in ret:
            ret[c] = 0
        ret[c] += 1
    return ret