def first_duplicate(nums: list[int]) -> int | None:
    if not nums:
        return None
    
    lista_no_dup = []

    for num in nums:
        if num  not in lista_no_dup:
            lista_no_dup.append(num)
        else:
            return num




if __name__=="__main__":

    lista_num = [1, 87, 58, 87, 4, 2, 8]


    print(first_duplicate(lista_num))