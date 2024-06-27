from typing import (
    List,
)

def find_peak(a: List[int]) -> int:
    if not a:
        return -1

    start, end = 0, len(a) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        # 这个地方很tricky 如果右边一直递增，则最后峰值在尾部
        # 如果右边不递增，则峰值在不递增的位置
        # 左边同理
        if a[mid] < a[mid + 1]:
            start = mid
        else:
            end = mid
    return start if a[start] > a[end] else end


print(find_peak([13,15,19,21,22,21,7]))