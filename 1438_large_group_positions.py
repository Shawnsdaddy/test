from typing import List


def large_group_positions(s: str) -> List[List[int]]:
    res = []
    startIndex = 0
    for index, char in enumerate(s):
        if char == s[startIndex]:
            pass
        else:
            if index > startIndex + 2:
                res.append([startIndex, index-1])
            startIndex = index
    if len(s) > startIndex + 2:
        res.append([startIndex, len(s) - 1])
    return res
print(large_group_positions("aa"))
