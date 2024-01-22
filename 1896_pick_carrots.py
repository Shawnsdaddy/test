from typing import (
    List,
)

def pick_carrots(carrot: List[List[int]]) -> int:
    i = (len(carrot)-1)//2
    j = (len(carrot[i])-1)//2
    res = carrot[i][j]
    carrot[i][j] = 0
    max,index = set_value(carrot,i,j)
    while max !=0:
        print(res)
        res += max
        max,index = set_value(carrot,index[0],index[1])
    return res

def set_value(carrot,i,j):
    max = 0
    index = (i,j)
    if i-1>=0:
        up = carrot[i-1][j]
    else:
        up = 0
    if up !=0:
        max = up
        index = (i-1,j)
    if i+1<len(carrot):
        down = carrot[i+1][j]
    else:
        down = 0
    if down>max :
        max = down
        index = (i+1,j)
    if j-1>=0:
        left = carrot[i][j-1]
    else:
        left = 0
    if left>max :
        max = left
        index = (i,j-1)
    if j+1<len(carrot[i]):
        right = carrot[i][j+1]
    else:
        right = 0
    if right>max :
        max = right
        index = (i,j+1)
    if max !=0:
        carrot[index[0]][index[1]] = 0
        return max, index
    else:
        return 0, (i,j)

carrot = [[5, 7, 6, 3],
[2,  4, 8, 12],
[3, 5, 10, 7],
[4, 16, 4, 17]]

print(pick_carrots(carrot))



