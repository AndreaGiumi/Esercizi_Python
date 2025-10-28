def head(lines: list[str], n: int) -> list[str]:
    filename = 'textio_head.txt'

    with open(filename, "w", encoding="utf-8") as file:
        for riga in lines:
            file.write(riga + "\n")

    
    with open(filename, "r", encoding="utf-8") as file:
        righe = []

        for i, riga in enumerate(file):
            if i >= n:
                break
            righe.append(riga.strip())
    return righe