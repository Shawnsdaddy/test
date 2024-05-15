from typing import (
    List,
)

def subarray_sum(nums: List[int]) -> List[int]:
    sum_dict = {0:-1}
    prefix_sum = 0
    for i in range(len(nums)):
        current_sum = prefix_sum + nums[i]
        if current_sum in sum_dict:
            return [sum_dict[current_sum]+1, i]
        else:
            sum_dict[current_sum] = i
        prefix_sum = current_sum
        print(sum_dict)

print(subarray_sum([-3, 1, -4, 2, -3, 4]))