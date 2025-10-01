def deep_get(d: dict | list, path: list, default=None):
    current = d
    if not current:
         return default
    for step in path:
            if isinstance(current, dict):
                current = current[step]
            elif isinstance(current, list) and isinstance(step, int):
                current = current[step]
            else:
                return default
    return current

    
