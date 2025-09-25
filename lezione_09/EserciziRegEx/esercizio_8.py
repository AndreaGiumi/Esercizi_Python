import re
def find_codes(text: str):
    _text = re.findall(r"[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{2}|\d+|[A-Z]{8}", text)
    return _text


text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
print(find_codes(text))
