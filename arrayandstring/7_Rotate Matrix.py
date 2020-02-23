def rotate_matrix(matrix):
    n = len(matrix)
    matrix1 = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix1[i][j] = matrix[j][n - i - 1]
    return matrix1


n = int(input())
matrix = [[] for i in range(n)]
for i in range(n):
    matrix[i] = [int(j) for j in input().split()]
matrix = rotate_matrix(matrix)
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
