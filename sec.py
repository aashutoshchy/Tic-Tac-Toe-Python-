import random

board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

winPatterns = [
  [0, 1, 2],
  [0, 3, 6],
  [0, 4, 8],
  [1, 4, 7],
  [2, 5, 8],
  [2, 4, 6],
  [3, 4, 5],
  [6, 7, 8],
];

currentPlayer = "X"
gameRunning = True

# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9) 
    print(board[6] + " | " + board[7] + " | " + board[8])

# take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    # Checking if the number is out of range
    if inp >= 1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops! Something went wrong.")

   
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Its a tie")
        gameRunning = False

# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

def checkWin(board):
    for pattern in winPatterns:
        pos1 = board[pattern[0]]
        pos2 = board[pattern[1]]
        pos3 = board[pattern[2]]
        if pos1 != "-" and pos2 != "-" and pos3 != "-":
            if pos1 == pos2 == pos3:
                print(f"The winner is {pos1}")

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin(board)
    checkTie(board)
