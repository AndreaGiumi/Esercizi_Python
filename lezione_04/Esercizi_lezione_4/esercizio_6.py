import random
import string
def psw_generator(lunghezza: int, use_upper: bool, use_digits: bool, use_symbol: bool) -> str:
    char: str = string.ascii_lowercase

    if use_upper:
        char += string.ascii_uppercase

    if use_digits:
        char += string.digits

    if use_symbol:
        char += string.punctuation


    password: str = ""


    for i in range(lunghezza):
        password += random.choice(char)


    
    return password


print(psw_generator(10, True, False, False))