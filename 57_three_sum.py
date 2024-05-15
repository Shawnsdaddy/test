from typing import (
    List,
)


def three_sum(self, numbers: List[int]) -> List[List[int]]:
    # write your code here
    numbers.sort()
    n = len(numbers)
    res = []
    if n < 3:
        return res
    for i in range(n - 2):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue
        total = 0 - numbers[i]
        left_index = i + 1
        right_index = n - 1
        while left_index < right_index:
            total = numbers[i] + numbers[left_index] + numbers[right_index]
            if total < 0:
                left_index += 1
            elif total > 0:
                right_index -= 1
            else:
                res.append([numbers[i], numbers[left_index], numbers[right_index]])
                while left_index + 1 < n - 1 and numbers[left_index] == numbers[left_index + 1]:
                    left_index += 1
                while right_index - 1 > 0 and numbers[right_index] == numbers[right_index - 1]:
                    right_index -= 1
                left_index += 1
                right_index -= 1
    return res


