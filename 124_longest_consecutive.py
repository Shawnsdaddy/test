def longest_consecutive(nums):
    longest, num_set = 0, set(nums)
    for n in nums:
        if n-1 not in num_set:
            k = 1
            while n+1 in num_set:
                k+=1
                n+=1
            if k > longest:
                longest = k 

    return longest

