def parse_int_list_strict(s: str) -> list[int]:
    if not s:
        return []
    result = []
    for t  in s.split(","):
        t.strip()
        result.append(int(t))

    return result