from typing import (
    List,
)

def longest_common_prefix(strs: List[str]) -> str:
        # write your code here
    start = 0
    error = False
    res=""
    while not error:
        if not strs:
            error = True
        for index, v in enumerate(strs):
            if len(v)< start+1:
                error = True
                break
            if index == 0:
                common = strs[0][start]
            if common!= strs[index][start]:
                error= True
                break
        if not error:
            res += common
        start+=1
    return res

print(longest_common_prefix(["ABCDEFG", "ABCEFG", "ABCEFA"]))