def pick(d: dict, keys: list[str]) -> dict:
    new_d = {}
    for k in keys:
        if k in d:
            new_d[k] = d[k]
    return new_d