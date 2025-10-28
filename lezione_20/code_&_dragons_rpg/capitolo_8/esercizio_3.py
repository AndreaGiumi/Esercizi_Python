def sum_numbers(obj: int | float | list | tuple | dict) -> float:
    if isinstance(obj, (int, float)):
        return obj
    
    elif isinstance(obj, (list, tuple)):
        for x in obj:
            return sum(sum_numbers(x))
    
    elif isinstance(obj, dict):
        for v in obj.values():
            return sum(sum_numbers(v))
    else:
        return 0
    