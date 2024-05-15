from typing import (
    List,
)


def first_missing_positive(a: List[int]) -> int:
    a.sort()
    res = 1
    for i in range(len(a)):
        if a[i] > res:
            break
        if a[i] > 0 and res == a[i]:
            res += 1
    return res


def first_missing_positive_1(a: List[int]) -> int:
    n = len(a)
    # 1,2,3,4,5,6

    for i in range(len(a)):
        if a[i] <= 0 or a[i] > n:
            a[i] = n + 1
    print(a)
    for i in range(len(a)):
        num = a[i]
        if num <= n:
            a[num-1] = - abs(a[num-1])
    print(a)
    for i in range(n):
        if a[i]>0:
            return i+1
    return n+1


print(first_missing_positive_1([1, 2, 0]))
