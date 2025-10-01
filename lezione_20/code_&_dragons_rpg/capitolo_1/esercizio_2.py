def max_or_none(nums: list[int]) -> int:
    if not nums:
        return None
    else:
        massimo = max(nums)
        return massimo