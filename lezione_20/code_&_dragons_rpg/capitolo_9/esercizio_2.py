def read_safe(text: str | None, default: str = '') -> str:
    if text is None:
        return default
    return text