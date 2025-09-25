frase = (input("Inserisci frase: "))

match frase:
    case frase if frase[-1] == "?" and len(frase) % 2 == 0:
        print("Si")
    case frase if frase[-1] == "?" and len(frase) % 2 != 0:
        print("No")
    case frase if frase[-1] == "!":
        print("Wow!")
    case _:
        print("Tu dici " + f'"{frase}"')



# match frase[-1]:
#     case "?" if len(frase) % 2 == 0:
#         print("Si")
#     case "?" if len(frase) % 2 != 0:
#         print("No")