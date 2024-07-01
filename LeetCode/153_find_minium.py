from typing import List


def find_minimu(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    # find max and next index is the minium
    while left +1 < right:
        mid = left + (right - left) // 2
        if nums[left]< nums[mid]:
            left = mid
        else:
            right = mid
    print(left,right)
    if nums[left]>nums[right]:
        return nums[right]
    else:
        if right == len(nums)-1:
            return nums[0]
        else:
            return nums[right+1]
            
print(find_minimu([2,3,4,5,1]))
    