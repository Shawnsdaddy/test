from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def search_2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    if nums[left]== target:
        return left
    return -1

def search_2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left +1 < right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid
    if nums[left]== target:
        return left
    if nums[right] == target:
        return right    
    return -1


print(search([-1,0,3,5,9,12],9))