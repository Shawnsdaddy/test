def longest_common_substring(a: str, b: str) -> int:
    rows, cols = len(a)+1, len(b)+1
    array = [[0 for _ in range(cols)] for _ in range(rows)]
    res = 0
    for row in range(1,rows):
        for col in range(1,cols):
            if a[row-1] == b[col-1]:
                array[row][col] = array[row-1][col-1]+1
                res = max(res,array[row][col])
                continue
            array[row][col] = 0
    return res


print(longest_common_substring("abc","a"))

