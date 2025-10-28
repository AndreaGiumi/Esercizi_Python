def chunk_sums(nums: list[int], size: int) -> list[int]:

    if size < 1:
        return []
    
    if not nums:
        return []
    

    final_lista = []

    new_lista = []

    for num in nums:
        new_lista.append(num)
        if len(new_lista) == size:
            final_lista.append(sum(new_lista))
            new_lista = []
    if new_lista:
        final_lista.append(sum(new_lista))
    return final_lista



lista_num =[2, 34, 5, 67, 7, 8, 33, 21, 1]
size = 4

print(chunk_sums(lista_num, size))
        
        
