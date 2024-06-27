def mergeSortedArray(A, m, B, n):
    dummy = []
    i, j = 0, 0
    while i < m and j < n:
        if A[i] < B[j]:
            dummy.append(A[i])
            i += 1
        else:
            dummy.append(B[j])
            j += 1
    if i < m:
        while i < m:
            dummy.append(A[i])
            i += 1
    if j < n:
        while j < n:
            dummy.append(B[j])
            j += 1
    z = 0
    for z in range(len(dummy)):
        A[z] = dummy[z]

    # if j < n :
    #     A.extend(B[j:])


A = [1, 3, 4, 6, 0, 0]


# 试一试双指针
def mergeSortedArray_2(A, m, B, n):
    p1, p2 = m - 1, n - 1
    tail = m + n - 1
    while p1 >= 0 or p2 >= 0:
        if p1 == -1:
            A[tail] = B[p2]
            p2 -= 1
        elif p2 == -1:
            A[tail] = A[p1]
            p1 -= 1
        elif A[p1] > B[p2]:
            A[tail] = A[p1]
            p1 -= 1
        else:
            A[tail] = B[p2]
            p2 -= 1
        tail -= 1


mergeSortedArray_2(A, 4, [2, 5], 2)
print(A)
