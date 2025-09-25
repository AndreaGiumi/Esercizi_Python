num_bambini: int = int(input("Inserisci numero di bambini: "))
match num_bambini:
    # n = 1
    case 1:
        print("Congratulazioni!")
    # n = 2
    case 2:
        print("Wow! Gemelli!")
    # n = 3
    case 3:
        print("Wow! Tre!")
    # n = 4
    case 4:
        print("Mamma Mia Quattro! Wow!")
    # n = 5
    case 5:
        print("Incredibile! Cinque!")
    # default case
    case _:
        print(f"Non ci credo! {num_bambini} bambini!")