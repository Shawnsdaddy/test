def removeElement(A, elem):
    n = len(A)
    i = 0
    while i < n:
        if i > len(A) - 1:
            break
        if A[i] == elem:
            del A[i]
            continue
        else:
            i += 1
    return len(A)


removeElement([1], "A")
