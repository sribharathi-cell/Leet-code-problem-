board = []

for i in range(9):
    board.append(input().split())

for i in range(9):
    row = set()
    col = set()

    for j in range(9):
        if board[i][j] != ".":
            if board[i][j] in row:
                print(False)
                exit()
            row.add(board[i][j])

        if board[j][i] != ".":
            if board[j][i] in col:
                print(False)
                exit()
            col.add(board[j][i])

print(True)
