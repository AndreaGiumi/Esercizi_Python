def count_lines(lines: list[str]) -> int:
    filename = 'textio_count.txt'
    
    with open(filename, "w", encoding="utf-8") as file:
        for riga in lines:
            file.write(riga + "\n")

    with open(filename, "r", encoding="utf-8") as file:
        count = 0

        for riga in file:
            count += 1
    return count