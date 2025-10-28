def filter_and_concat(nums: list[int], min_val: int) -> str:
    new_vals = ""
    for num in nums:
        if num > min_val:
            if new_vals:  
                new_vals += ","
            new_vals += str(num)
            print(type(num))
    print(new_vals) 




lista_num = [23, 4, 55, 6, 54, 2, 1, 66, 7, 89]

filter_and_concat(lista_num, 24)