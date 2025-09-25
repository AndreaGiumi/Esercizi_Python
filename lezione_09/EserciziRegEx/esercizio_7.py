import re

def is_valid_name(name: str):
    if re.findall(r"[A-Z][a-z]{2,}", name):
        return True
    else:
        return False
    




print(is_valid_name("Marco"))    # True
print(is_valid_name("marco"))    # False
print(is_valid_name("MAAAA"))     # False