def sqrt_mine(x: int) -> int:
    res = 0
    while res * res <= x:
        res +=1

    return res-1

def sqrt(x: int) -> int:
    l, r, ans = 0, x, -1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

print(sqrt(4))