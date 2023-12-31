def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):

    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]


    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        row = int(input("Выберите номер строки (0-2): "))
        col = int(input("Выберите номер столбца (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Выбранная ячейка уже занята. Попробуйте еще раз.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Игрок", winner, "победил!")
            game_over = True
        elif all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("Ничья!")
            game_over = True

        current_player = "O" if current_player == "X" else "X"

play_game()