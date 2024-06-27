def reverse_integer(n: int) -> int:
    negative = False
    if n<0:
        negative = True
    if negative:
        n = 0-n
    strInt = str(n)

    res = 0
    for index, char in enumerate(strInt):
        res+= (int(char))* 10**(index)
    if res > (2**32)-1:
        return 0
    else :return res if not negative else 0-res

print(reverse_integer(-123))