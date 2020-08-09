def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = []
    cols = []

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.append(x)
                cols.append(y)

    for row in rows:
        nullify_row(matrix, row)

    for col in cols:
        nullify_col(matrix, col)

    return matrix


def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0
