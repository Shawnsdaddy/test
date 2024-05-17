from typing import (
    List,
)


def search_matrix_old(matrix: List[List[int]], target: int) -> bool:
    def binary_search(nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                return [mid]
        if nums[right] == target:
            return [right]
        if nums[left] == target:
            return [left]
        return [left, right]

    m = len(matrix)
    if m == 0:
        return False
    first_elements = [row[0] for row in matrix]
    res = binary_search(first_elements, target)
    if len(res) == 1:
        return True
    else:
        idx = res[1] if matrix[res[1]][0] < target else  res[0]
        res = binary_search(matrix[idx], target)
        if len(res) == 1:
            return True
        else:
            return False
def search_matrix(matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    left = 0
    right = m*n -1
    while left + 1 < right:
        mid = (left+ right)//2
        x = mid // n
        y = mid - x * n
        mid_element = matrix[x][y]
        if mid_element > target:
            right = mid
        elif mid_element < target:
            left = mid
        else:
            return True
    if matrix[left//n][left - left//n * n] == target or matrix[right//n][right - right//n * n]== target:
        return True
    return False


print(search_matrix([[1,5,8,12,13,15,18,20,25,26,28,33,38,40,43,49,52,53,59],[84,100,110,129,141,156,177,198,220,242,254,266,284,297,316,326,343,358,373],[388,398,419,439,449,460,472,495,516,539,560,582,600,610,624,643,668,691,710],[720,733,751,765,787,804,814,832,856,880,905,930,950,974,999,1012,1022,1039,1061],[1081,1091,1102,1126,1151,1175,1194,1219,1239,1253,1263,1274,1287,1298,1308,1318,1337,1361,1382],[1404,1417,1437,1452,1466,1487,1503,1518,1537,1555,1578,1590,1601,1613,1636,1659,1669,1688,1712]],1888))

# write your code here
