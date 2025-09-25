import random
def genera(n: int) -> list[list[int]]:
    mat: list[list[int]] = []

    for r in range(n):
        row: list[int] = []
        for c in range(n):
            while True:
                x: int = random.randint(0,13)
                if c == 0:
                    row.append(x)
                    break
                if x != row[0] :
                    row.append(x)
                    break
        mat.append(row)

    return mat


def printMAT(mat: list[list[int]]) -> None:

    for r in range(len(mat)):
        for c in range(len(mat[r])):
            print(f"{mat[r][c]:<5}", end="")
        print("\n")

def calcolaCarico(mat: list[list[int]], r: int, c: int) -> int:
    s_r = sum(mat[r])
    s_c = 0
    for i in range(len(mat)):
        s_c += mat[i][c]
    k = s_r - s_c
    return k


def caricoNullo(mat: list[list[int]]) -> list[tuple[int]]:

    list_null: list[tuple[int]] = []

    for r in range(len(mat)):
        for c in range(len(mat)):
            if calcolaCarico(mat, r, c) == 0:
                list_null.append((r, c))
    return f"k_null {list_null}"


def caricoMax(mat: list[list[int]]) -> tuple[int]:
    calc_m = 0
    for r in range(len(mat)):
        for c in range(len(mat)):
            if calcolaCarico(mat, r, c) > calc_m:
                calc_m = calcolaCarico(mat, r, c)
             

    return calc_m




def caricoMin(mat: list[list[int]]) -> tuple[int]:
    calc_min = 0
    for r in range(len(mat)):
        for c in range(len(mat)):
            if calcolaCarico(mat, r, c) < calc_min:
                calc_min = calcolaCarico(mat, r, c)
             

    return calc_min


    
    















if __name__ == "__main__":

    mat = genera(5)
    printMAT(mat)
    print(calcolaCarico(mat, 2, 2))
    caricoMax(mat)
    print(caricoNullo(mat))
    print(caricoMax(mat))
    print(caricoMin(mat))


