def find_max(nums):
    max_so_far = float("-inf")
    for i in range(0, len(nums)):
        if max_so_far < nums[i]:
            max_so_far = nums[i]
    return max_so_far
