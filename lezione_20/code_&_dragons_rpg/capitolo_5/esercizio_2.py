def count_even(nums: list[int]) -> int:
    lista_even = []
    for i in nums:
        if i % 2 == 0:
            lista_even.append(i)

    return len(lista_even)


lista_num = [2, 34, 5, 6, 1, 0, 23, 4]

print(count_even(lista_num))