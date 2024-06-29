from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    y_index = m - 1
    x_index = 0
    while x_index < y_index:
        mid = x_index + (y_index - x_index) // 2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target:
            x_index = mid + 1
        else:
            y_index = mid
    row_index = x_index
    if matrix[x_index][0] == target:
        return True
    elif matrix[x_index][0] > target:
        row_index = x_index - 1
    j = 0
    while j < n:
        mid = j + (n - j) // 2
        if matrix[row_index][mid] == target:
            return True
        elif matrix[row_index][mid] < target:
            j = mid + 1
        else:
            n = mid
    if j < len(matrix[0]) and matrix[row_index][j] == target:
        return True
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 30))