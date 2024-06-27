from typing import (
    List,
)


def three_sum(numbers: List[int], target: int) -> int:
    # write your code here
    numbers.sort()
    n = len(numbers)
    closest = float('inf')
    res = float('inf')
    for i in range(n - 2):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue
        left_index = i + 1
        right_index = n - 1
        while left_index < right_index:
            total = numbers[i] + numbers[left_index] + numbers[right_index]
            diff = total - target
            if diff == 0:
                return total
            elif diff < 0:
                left_index += 1
                diff = 0 - diff
            else:
                right_index -= 1
            if diff < closest:
                closest = diff
                res = total
    return res


print(three_sum([1, 0, -1, -1, -1, -1, 0, 1, 1, 1, 2], 7))


def threeSumClosest(numbers, target):
    numbers.sort()
    ans = None
    for i in range(len(numbers)):
        left, right = i + 1, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right] + numbers[i]
            if ans is None or abs(sum - target) < abs(ans - target):
                ans = sum

            if sum <= target:
                left += 1
            else:
                right -= 1
    return ans
