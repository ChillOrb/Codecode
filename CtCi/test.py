letters = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "BCCED"


def exist(board, word):
    if not word:
        return True
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if search_word_util(board, i, j, word):
                return True
    return False


def search_word_util(board, row, col, word):
    if len(word) == 0:
        return True

    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[0]:
        return False

    board[row][col] = " "

    if search_word_util(board, row-1, col, word[1:]):
        return True
    if search_word_util(board, row+1, col, word[1:]):
        return True
    if search_word_util(board, row, col-1, word[1:]):
        return True
    if search_word_util(board, row, col+1, word[1:]):
        return True

    board[row][col] = word[0]
    return False


print(exist(letters, word))
