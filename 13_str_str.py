def str_str(source: str, target: str) -> int:
    n = len(target)
    for index, char in enumerate(source):
        if index+n <len(source) and source[index:index+n]==target:
            return index
    return -1

print(str_str("mississippi","3"))
