def zero_matrix(matrix, row_size, column_size):
    row = [0 for i in range(row_size)]
    column = [0 for i in range(column_size)]
    for i in range(row_size):
        for j in range(column_size):
            if matrix[i][j] == 0:
                row[i] = column[j] = 1
    for i in range(row_size):
        for j in range(column_size):
            if row[i] or column[j]:
                matrix[i][j] = 0


size_of_rows = int(input())
size_of_columns = int(input())
matrix = []
for i in range(size_of_rows):
    columns = [int(i) for i in input().split()]
    matrix.append(columns)
zero_matrix(matrix, size_of_rows, size_of_columns)
for i in range(size_of_rows):
    for j in range(size_of_columns):
        print(matrix[i][j], end=' ')
    print()
