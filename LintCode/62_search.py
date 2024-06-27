from typing import (
    List,
)

def search(nums: List[int],target) -> int:
    left = 0
    right = len(nums)-1
    if right == -1:
        return -1
    while left +1 < right:
        mid = (left+ right)//2
        # if target == nums[mid]:
        #     return mid
        if nums[right] > nums[mid] > nums[left]:
            if target > nums[mid]:
                left = mid
            else:
                right = mid

        elif nums[left] > nums[mid]:
            if target > nums[mid] and target<=nums[right]:
                left = mid
            else:
                right = mid
        else:
            if target > nums[left] and target<=nums[mid]:
                right = mid
            else:
                left = mid
    if nums[left] == target:
        return left
    elif nums[right]== target:
        return right
    else:
        return -1

print(search([6,8,9,1,3,5],5))