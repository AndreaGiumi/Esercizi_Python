def rle(s: str) -> list[tuple[str, int]]:
    new_s = s.replace(" ", "").lower()
    
    if new_s == "":
        return []
    
    result = []
    current_char = new_s[0]
    count = 1
    
    for char in new_s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    
    result.append((current_char, count))
    
    return result