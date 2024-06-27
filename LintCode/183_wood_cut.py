from typing import (
    List,
)
def can_cut(woods , k, max):
    sum = 0
    for wood in woods:
        sum += wood//max
    return sum == k

def wood_cut(woods: List[int],k) -> int:
    l = 0
    for wood in woods :
        l += wood
    right = l//k
    left = 0
    while left + 1 < right:
        mid = (left+right)//2
        if mid <=0:
            break
        if can_cut(woods,k,mid):
            left = mid
        else:
            right = mid
    if right >0 and can_cut(woods,k,right):
        return right
    else:
        return left

def can_cut(woods , k, max):
    sum = 0
    for wood in woods:
        sum += wood//max
    return sum >= k

print(wood_cut([232,124,456],7))