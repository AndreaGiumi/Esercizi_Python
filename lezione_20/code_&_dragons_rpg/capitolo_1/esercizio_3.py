    
def dedup_stable(nums: list[int]) -> list[int]:
    lista_no_dup =  [nums[0]]
    if not nums:
        return []
    else:
        for i in nums[1:]:
           if i != lista_no_dup[-1]:
               lista_no_dup.append(i)
        return lista_no_dup


if __name__=="__main__":
    lista_num = [2,2, 1, 2, 2, 5, 4, 4 ,58]


    print(dedup_stable(lista_num))