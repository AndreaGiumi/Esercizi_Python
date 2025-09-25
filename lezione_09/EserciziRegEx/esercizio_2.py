import re
def  extract_emails(text:str):
    email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-z]{2,}", text)
    return email

text = "Contattaci a info@azienda.com oppure support@help.org"
print(extract_emails(text))




