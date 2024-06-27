def compare_strings(a: str, b: str) -> bool:
    a = sorted(a)
    b = sorted(b)
    while len(b)>0 and len(a)>0:
        if b[0] == a[0]:
            b = b[1:]
            a = a[1:]
        else:
            a = a[1:]
    return len(b)==0

print(compare_strings("ABCD","AABC"))