def write_and_read(lines: list[str]) -> list[str]:
    filename = 'textio_write_and_read.txt'
    with open(filename, "w", encoding="utf-8") as file:
        for riga in lines:
           file.write(riga + "\n")

    righe = []
    with open(filename, "r", encoding="utf-8") as file:
        for riga in file:
            righe.append(riga.strip())
    return righe


    


