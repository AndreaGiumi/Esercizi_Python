def unique_count(nums: list[int]) -> int:
    list_no_dup = []
    if not nums:
        return []

    for num in nums:
        if num not in list_no_dup:
            list_no_dup.append(num)
    return len(list_no_dup
)
