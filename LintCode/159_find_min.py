from typing import (
    List,
)

def find_min(nums: List[int]) -> int:
    left = 0
    right= len(nums)-1
    while left+1 <right:
        mid = (left + right) //2
        if nums[mid]<nums[right] and nums[left]< nums[mid]:
            right = mid
        elif nums[left] > nums[mid]:
            right = mid
        elif nums[right] < nums[left]:
            left = mid

    if nums[left] < nums[right]:
        return nums[left]
    else:
        return nums[right]

print(find_min([4, 5, 6, 7, 0, 1, 2]))