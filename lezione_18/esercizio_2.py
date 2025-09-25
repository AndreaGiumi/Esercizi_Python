def validate_password(password:str):
    if len(password) < 20:
        raise ValueError("La password è troppo corta: lunghezza minima di 20 caratteri")
    is_upper = 0
    for char in password:
        if char.isupper():
            is_upper += 1
    if is_upper < 3:
        raise ValueError("La password non rispetta i criteri richiesti: inserire almeno 3 caratteri maiuscoli")
    is_special = 0
    not_special = 0
    for symb in password:
        if symb.isalpha() or symb.isnumeric():
            not_special += 1
        else:
            is_special += 1
    if is_special < 4:
        raise ValueError("La password non rispetta i criteri richiesti: inserire almeno 4 caratteri speciali")
    
    return True



try:
    password = "W!!dfjhjkljhg56565hjkEljhgyuikjhuio"
    if validate_password(password):
        print("Password valida")
except ValueError as error:
    print(error)
