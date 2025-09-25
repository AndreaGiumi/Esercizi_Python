point: tuple[int] = ()

coordinata_X: int = int(input("Inserisci coordinata X: "))
coordinata_Y: int = int(input("Inserisci coordinata Y: "))

point = point + (coordinata_X , coordinata_Y)

# match point:
#     case point if point == (0, 0):
#         print(f"Il punto {point} si trova nell'origine.")
#     case point if point == (coordinata_X, 0):
#         print(f"Il punto {point} si trova sull'asse X.")
#     case point if point == (0, coordinata_Y):
#         print(f"Il punto {point} si trova sull'asse Y.")
#     case coordinata_X, coordinata_Y if coordinata_X > 0 and coordinata_Y > 0:
#         print(f"Il punto {point} si trova nel primo quadrante.")
#     case coordinata_X, coordinata_Y if coordinata_X < 0 and coordinata_Y > 0:
        # print(f"Il punto {point} si trova nel secondo quadrante.")
#     case coordinata_X, coordinata_Y if coordinata_X < 0 and coordinata_Y < 0:
        # print(f"Il punto {point} si trova nel terzo quadrante.")
#     case coordinata_X, coordinata_Y if coordinata_X > 0 and coordinata_Y < 0:
        # print(f"Il punto {point} si trova nel quarto quadrante."
#     case _:
#         print("Errore nella sintassi")


match point:
    case (0, 0):
        print(f"Il punto {point} si trova nell'origine.")
    case (coordinata_X, 0):
        print(f"Il punto {point} si trova sull'asse X.")
    case (0, coordinata_Y):
        print(f"Il punto {point} si trova sull'asse Y.")
    case (coordinata_X, coordinata_Y) if coordinata_X > 0 and coordinata_Y > 0:
        print(f"Il punto {point} si trova nel primo quadrante.")
    case (coordinata_X, coordinata_Y) if coordinata_X < 0 and coordinata_Y > 0:
        print(f"Il punto {point} si trova nel secondo quadrante.")
    case (coordinata_X, coordinata_Y) if coordinata_X < 0 and coordinata_Y < 0:
        print(f"Il punto {point} si trova nel terzo quadrante.")
    case (coordinata_X, coordinata_Y) if coordinata_X > 0 and coordinata_Y < 0:
        print(f"Il punto {point} si trova nel quarto quadrante.")
    case _:
        print("Errore nella sintassi")
    
          


    
    
    