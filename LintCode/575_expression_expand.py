def expression_expand(s: str) -> str:
    stack = []
    for c in s:
        if c !="]":
            stack.append(c)
        else:
            val = stack.pop()
            repeat = 1
            str = val
            while val !="[":
                val= stack.pop()
                str = val + str
            str = str[1:]
            index = 0
            if stack :
                repeat = 0
                while stack and stack[-1].isdigit():
                    repeat += (int)(stack.pop())*(10**index)
                    index+=1
            str = str* repeat
            for _c in str:
                stack.append(_c)

    return ''.join(stack)


print(expression_expand("3[2[ad]3[pf]]xyz"))