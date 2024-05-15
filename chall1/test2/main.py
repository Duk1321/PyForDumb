def find_min(nums):
    min_so_far = float("inf")

    for i in range(0, len(nums)):
        if nums[i] < min_so_far:
            min_so_far = nums[i]

    return min_so_far