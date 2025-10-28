def rotate_right(nums: list[int], k: int) -> list[int]:
    if len(nums) == 0:
        return []
    
    k = k % len(nums)
    
    if k == 0:
        return nums[:]
    
    return nums[-k:] + nums[:-k]