def are_anagrams(a: str, b: str) -> bool:
    new_a = a.lower().replace(" ", "")
    new_b = b.lower().replace(" ", "")
    if not new_a or not new_b:
        return False    
    if sorted(new_a) == sorted(new_b):
        return True
    return False

    

if __name__=="__main__":
    a = "Ciao a tutti"
    b = "Oaic a uttit"

    print(are_anagrams(a,b))