from typing import List


def groupAnagrams(strs):
    str_dict = {}
    for i in range(len(strs)):
        st = strs[i]
        sorted_str = ''.join(sorted(st))
        str_dict[sorted_str]=str_dict.get(sorted_str,[])
        str_dict[sorted_str].append(strs[i])
    print(str_dict)
    return list(str_dict.values())
