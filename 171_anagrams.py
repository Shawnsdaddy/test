from typing import (
    List,
)


def anagrams(strs: List[str]) -> List[str]:
    dict = {}
    n = 0
    one_time = {}
    while n < len(strs):
        m = ''.join(sorted(strs[n]))
        if m not in one_time and m not in dict:
            one_time[m] = strs[n]
            del strs[n]
            continue
        elif m in one_time:
            dict[m] = 2
            strs.append(one_time[m])
            del one_time[m]
        else:
            dict[m] += 1
        n += 1
    return strs


print(anagrams(["lint", "intl", "inlt", "code"]))
