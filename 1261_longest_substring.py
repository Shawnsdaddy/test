def longest_substring(s: str, k: int) -> int:
    for c in set(s):
        if s.count(c) < k:
            if len(s)==8:
                print(c)
                print(max(longest_substring(t, k) for t in s.split(c)))
            return max(longest_substring(t, k) for t in s.split(c))
    return len(s)



print(longest_substring("aaebcfbbc",2))


