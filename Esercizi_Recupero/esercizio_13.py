def is_valid_ipv4(address: str) -> bool:
    address = address.split(".")

    if len(address) != 4:
        return False
    
    for i in address:
        if not i.isdigit():
            return False

        if not (0<=int(i)<=255):
            return False
    return True




print(is_valid_ipv4("255.25a.255.255"))