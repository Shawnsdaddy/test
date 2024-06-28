from typing import List

def eval_r_p_n(tokens: List[str]) -> int:
    stack = []
    while tokens:
        if tokens[0] in ["+","-","*","/"]:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(eval(str(y) +tokens[0]+str(x))))
        else:
            stack.append(tokens[0])
        tokens = tokens[1:]
    return int(stack[0])

print(eval_r_p_n(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))