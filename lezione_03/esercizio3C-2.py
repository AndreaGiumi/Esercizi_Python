voto: int = int(input("Inserisci voto di laurea: "))

match voto:
    # # case 1
    # case 106|107|108|109|110:
    #     print("GPA 4.0")
    # # case 2
    # case 101|102|103|104|105:
    #     print("GPA 3.7")
    # # case 3
    # case 96|97|98|99|100:
    #     print("GPA 3.3")
    # # case 3
    # case 91|92|93|94|95:
    #     print("GPA 3.0")
    # # case 4
    # case 86|87|88|89|90:
    #     print("GPA 2.7")
    # # case 5
    # case 81|82|83|84|85:
    #     print("GPA 2.3")
    # # case 6
    # case 76|77|78|79|80:
    #     print("GPA 2.0")
    # # case 7
    # case 70|72|73|74|75:
    #     print("GPA 1.7")
    # # case 8
    # case 66|67|68|69:
    #     print("GPA 1.0")
    # # case default
    # case _:
    #     print("Voto non valido!")      


    case voto if voto >= 106 and voto <= 110: 
        print("GPA 4.0")
    case voto if voto >= 101 and voto <= 105:
        print("GPA 3.7")
    case voto if voto >= 96 and voto <= 100:
        print("GPA  3.3")
    case voto if voto >= 91 and voto <= 95:
        print("GPA 3.0")
    case voto if voto >= 86 and voto <=90:
        print("GPA 2.7")
    case voto if voto >= 81 and voto <= 85:
        print("GPA 2.3")
    case voto if voto >= 76 and voto <= 80:
        print("GPA 2.0")
    case voto if voto >= 70 and voto <= 75:
        print("GPA 1.7")
    case voto if voto >= 66 and voto <= 69:
        print("GPA 1.0")
    case _:
        print("Voto non valido!")