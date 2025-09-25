def sum_primary_diagonal(matrix: list[list[int]]) -> int:
    n = len(matrix)
    matr1 = []
    
    for i in range(n):
        matr1.append(matrix[i][i])
    print(sum(matr1))





mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

# sum_primary_diagonal(mat1)





def sum_secondary_diagonal(matrix: list[list[int]]) -> int:
    n = len(matrix)
    matr2 = []

    for i in range(n):
        matr2.append(matrix[i][n-1-i])
    print(sum(matr2))





mat2= [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]


sum_secondary_diagonal(mat2)







