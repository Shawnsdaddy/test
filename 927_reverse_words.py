def reverse_words(str: str) -> str:
    # write your code here
    return ' '.join(reversed(str.split(' ')))


print(reverse_words("hello my name is Li Lei"))
