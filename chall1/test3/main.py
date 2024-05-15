def remove_nonints(nums):
    result = []

    for i in range(0, len(nums)):
        if type(nums[i]) == int:
            result.append(nums[i])
    
    return result
