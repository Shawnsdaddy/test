from typing import (
    List,
)
def product_except_self(nums: List[int]) -> List[int]:
    res = [1]*len(nums)
    right_result = nums[-1]
    for n in range(1,len(nums)):
        res[n] = nums[n-1]*res[n-1]
    print(res)
    for i in range(len(nums)-1, -1, -1):
        if i != len(nums)-1:
            res[i] *=right_result
            right_result *= nums[i]
    return res 