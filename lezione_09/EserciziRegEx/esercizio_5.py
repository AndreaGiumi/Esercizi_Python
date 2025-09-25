import re
def find_dates(text: str):
    date = re.findall(r"[0-9]{2}+/[0-9]{2}+/[0-9]{4}", text)
    return date


text = "Le date importanti sono 09/04/2025 e 15/08/2023."
print(find_dates(text))