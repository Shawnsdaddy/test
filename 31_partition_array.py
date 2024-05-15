from typing import (
    List,
)


def partition_array(nums: List[int], k: int) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] >= k:
            if nums[right] >= k:
                right -= 1
                continue
            else:
                # 交换
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
        else:
            left += 1
    print(nums)
    for i in range(len(nums)):
        if nums[i] >= k:
            return i
    return len(nums)


print(partition_array([7,7,9,8,6,6,8,7,9,8,6,6],12))