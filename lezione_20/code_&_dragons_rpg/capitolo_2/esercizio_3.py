def invert_unique(d: dict) -> dict:
    for key, value in d.copy().items():
        if not d:
            return {}
        del d[key]
        d[value] = key
    return d    