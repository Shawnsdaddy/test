def fibonacci(n: int) -> int:
    initList = [0,1]
    if n <2:
        return initList[n]
    else:
        res = [0]*n
        res[1]=1
        for i in range(2,n):
            res[i] = res[i-1]+res[i-2]
    return res[n-1]

print(fibonacci(10))