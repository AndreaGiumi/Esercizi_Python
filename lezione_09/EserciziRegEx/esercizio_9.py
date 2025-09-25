import re

def find_fc(text: str):
    _cf = re.findall(r"[A-Z]{6}[0-9]{2}[A-EHLMPRST][0-9]{2}[A-Z0-9]{4}[A-Z]", text)
    return _cf


testo = "Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."

print(find_fc(testo))

