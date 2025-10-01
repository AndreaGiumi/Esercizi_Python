def get_or_default(d: dict, k, default=None):
    if not d:
        return default
    else:
        for key in d.keys():
            if k == key:
                return d[k]
            else:
                return default