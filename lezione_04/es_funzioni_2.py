def check_length(a:str):
    if len(a) > 10:
        print(f"La lunghezza di \"{a}\" è maggiore di 10")
    elif len(a) < 10:
        print(f"La lunghezza di \"{a}\" è minore di 10")
    else:
        print(f"La lunghezza di \"{a}\" è uguale a 10 ")



check_length("Ciaooooooo")