from typing import List


def name_deduplication(self, names: List[str]) -> List[str]:
    # write your code here
    ret = set()
    for i in names:
        ret.add(i.lower())
    return list(ret)