def removeDuplicates(nums):
    n = len(nums)
    i = 0
    while i < n:
        if i > len(nums)-2:
            break
        if nums[i]== nums[i+1]:
            del nums[i]
        else:
            i+=1

    return nums

print(removeDuplicates([1,1,2]))