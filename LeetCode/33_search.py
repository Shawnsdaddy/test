from typing import List


def search(nums: List[int], target: int) -> bool:
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] < nums[mid] < nums[right]:
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        elif nums[left] < nums[mid] and nums[mid] > nums[right]:
            if target < nums[left] or target > nums[mid]:
                left = mid
            else:
                right = mid
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid
            else:
                left = mid
    print(left, right)
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    else:
        return -1

