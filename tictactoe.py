# Tic-Tac-Toe Game in Python
# Jacob McAlee | February 19, 2026


def printBoard(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")


def checkWinner(board, player):
    winningCombinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for combo in winningCombinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
        return False
    

def ticTacToe():
    board = [" " for _ in range(9)]
    currentPlayer = "X"

    print("Tic-Tac-Toe")
    print("=" * 10)
    print("This is what the board looks like")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|-- ")
    print(" 7 | 8 | 9 ")
    print("=" * 10)

    for turn in range(9):
        printBoard(board)

        try:
            move = int(input(f"Player {currentPlayer}, Choose Position 1-9: ")) - 1

            if move < 0 or move > 8:
                print("Position Not Valid, Try Again")
                continue

            if board[move] != " ":
                print("Spot is Already taken, try Again.")
                continue

            board[move] = currentPlayer

            if checkWinner(board, currentPlayer):
                printBoard(board)
                print(f"Player {currentPlayer} Wins !")
                return
            
            currentPlayer = "0" if currentPlayer == "X" else "X"

        except ValueError:
            print("Enter a Valid Number.")

    printBoard(board)
    print("Its a Draw.")


if __name__ == "__main__":
    ticTacToe()