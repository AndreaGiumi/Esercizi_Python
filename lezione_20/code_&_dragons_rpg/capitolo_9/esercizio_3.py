def safe_parse_int_list(s: str) -> list[int]:
    result = []
    for token in s.split(','):
        token = token.strip()
        try:
            result.append(int(token))
        except (ValueError, TypeError):
            pass
    return result



