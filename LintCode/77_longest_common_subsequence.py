def longest_common_subsequence( a: str, b: str) -> int:
    # write your code here
    rows, cols = len(a) + 1, len(b) + 1
    array = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(1, rows):
        for col in range(1, cols):
            if a[row - 1] == b[col - 1]:
                array[row][col] = array[row - 1][col - 1] + 1
                continue
            array[row][col] = max(array[row - 1][col], array[row][col - 1])
    return array[len(a)][len(b)]

print(longest_common_subsequence("ABCD","EACB"))