matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def searchele(matrix, ele):
    r, c = 0, 2
    while r <= 2 and c >= 0:
        if matrix[r][c] < ele:
            r += 1

        elif matrix[r][c] > ele:
            c -= 1

        elif matrix[r][c] == ele:
            return r, c

        else:
            return True
    return False


x = searchele(matrix, 7)

print(x)
