from typing import (
    List,
)


def search_range(a: List[int], target: int) -> List[int]:
    left = 0
    right = len(a) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if a[mid] >= target:
            right = mid
        else:
            left = mid
    left_bound = -1
    if a[left] == target:
        left_bound = left
    elif a[right] == target:
        left_bound = right
    start, end = left_bound, len(a) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if a[mid] <= target:
            start = mid
        else:
            end = mid
    right_bound = -1
    if a[end] == target:
        right_bound = end
    elif a[start] == target:
        right_bound = start
    elif left_bound != -1:
        right_bound = left_bound
    return [left_bound, right_bound]


print(search_range([-1,0,1,2,2,2,3,3,3,4,4,4,5,5,6,90,92,93,101], 2))
