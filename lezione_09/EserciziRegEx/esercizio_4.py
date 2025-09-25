import re
def is_valid_cap(cap: str):
    if re.findall(r"\w{5}", cap):
        return True
    else:
         return False
    
    

print(is_valid_cap("5475D"))