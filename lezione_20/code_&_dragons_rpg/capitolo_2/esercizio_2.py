def merge_overwrite(a: dict, b: dict) -> dict:
    a.update(b)
    return a


if __name__=="__main__":

    a = {"Ciao" : 5}
    b = {"doia" : 65, "mamma":665}


    print(merge_overwrite(a, b))