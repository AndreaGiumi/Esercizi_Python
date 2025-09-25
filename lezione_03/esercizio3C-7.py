i = 0
testa: int = 0
croce: int = 0
while i < 8:
    lancio: str = str(input("Scegli testa o croce: "))
    i += 1
    match lancio:
        case "t"| "T":
            testa += 1
        case "c"| "C":
            croce += 1
percentuale_testa: float = (testa * 100) / 8 
percentuale_corce: float = (croce * 100) / 8

print(f"Totale lanci testa = {testa}")
print(f"Totale lanci corce = {croce}")
print(f"Percentuale lanci testa = {percentuale_testa:.2f} %")
print(f"PErcentuale lanci croce = {percentuale_corce:.2f} %")