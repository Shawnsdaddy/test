def longest_palindrome(s: str) -> str:
    # write your code here
    res = ""
    for index, char in enumerate(s):
        j = 0
        ## 奇数情况
        while index - j >= 0 and index + j < len(s) and s[index - j] == s[index + j] :
            j +=1
        if len(res)<2*j-1:
            maxj = j-1
            maxIndex = index
            res = s[maxIndex - maxj:maxIndex + maxj+1]
        ## 偶数请看
        j = 1
        while index + j < len(s) and index + j < len(s) and s[index] == s[index + j] :
            j +=1
        if len(res)<=2*(j-1):
            maxj = j-1
            maxIndex = index
            res = s[maxIndex:maxIndex + maxj+1]
    return res

print(longest_palindrome("aaaa"))