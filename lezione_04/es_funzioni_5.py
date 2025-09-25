def add_one(mynum: int) -> int:
    return mynum + 1  
   

def add_one_to_list(myList:list[int]):
    new_list:list[int] = []
    for elem in myList:
        new_list.append(add_one(elem))
    print(new_list) 
ciao = [2, 5, 4]
new_list:list[int] =  add_one_to_list(ciao)

