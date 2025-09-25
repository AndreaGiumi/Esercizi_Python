import re
def mask_numbers(text: str):
    sost = re.sub(r"\d", "#", text)
    return sost


text = "Il codice è 12345 e la data è 2025."
print(mask_numbers(text))