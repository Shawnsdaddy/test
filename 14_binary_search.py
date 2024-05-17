from typing import (
    List,
)


def binary_search_wrong(nums: List[int], target: int) -> int:
    # wrong
    min_index = None

    def helper(nums, target, start_index=0):
        global min_index
        mid = len(nums) // 2
        if mid == 0 and nums[mid] != target:
            return
        if nums[mid] > target:
            return binary_search(nums[:mid], target, 0)
        elif nums[mid] < target:
            return binary_search(nums[mid:], target, mid)
        else:
            return start_index + mid

    return helper(nums, target, 0)


def binary_search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)
    while left + 1< right:
        mid = (left+right)//2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid
    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right
    else :
        return  - 1



print(binary_search([3, 4, 5, 8, 8, 8, 8, 10, 13, 14], 8))
