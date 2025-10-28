def copy_list(src: list[str]) -> list[str]:
    source_file = 'textio_source.txt'
    copy_file = 'textio_copy.txt'
    
    with open(source_file, "w", encoding="utf-8") as file:
        for riga in src:
            file.write(riga + "\n")

    
    with open(copy_file, "w", encoding="utf-8") as file:
        for riga in src:
            file.write(riga + "\n")

    with open(copy_file, "r", encoding="utf-8") as file:
        righe = []
        for riga in file:
            righe.append(riga.strip())
    return righe

        

    