from typing import (
    List,
)

def search_insert(a: List[int], target: int) -> int:
    # write your code here
    left = 0
    right = len(a)
    while left + 1 < right:
        mid = (left+right)//2
        if a[mid]> target:
            right = mid
        elif a[mid] < target:
            left = mid
        else:
            return mid

    if a[left]>= target:
        return left
    else:
        return right
