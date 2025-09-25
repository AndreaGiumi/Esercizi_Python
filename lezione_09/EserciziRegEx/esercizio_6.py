import re

def check_product_code(code: str):
    if re.findall(r"[A-Z]{4}+-[0-9]{4}+-[A-Z]{2}", code):
        return True
    else:
        return False


print(check_product_code("PROD-9876-ZX"))
print(check_product_code("PROD-99-ZX"))