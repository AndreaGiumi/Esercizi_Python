def contains_line(lines: list[str], needle: str) -> bool:
    filename = 'textio_contains.txt'
    
    with open(filename, "w", encoding="utf-8") as file:
        for riga in lines:
            file.write(riga + "\n")

    
    with open(filename, "r", encoding="utf-8") as file:
        for riga in file:
            if riga.strip() == needle:
                return True
    return False