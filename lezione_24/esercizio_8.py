def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    '''Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori'''
    new_dict = {}
    for key, value in dict1.items():
        if key not in dict2:
            new_dict[key] = value
        else:
            new_dict[key] = dict1[key] + dict2[key]

    for key, value in dict2.items():
        if key not in dict1:
            new_dict[key] = value
    return new_dict        
                
if __name__=="__main__":
    print(merge_dictionaries({"a" : 1}, {"b" : 2}))