def printBoard(xState, yState):
    print(f"0 | 1 | 2")
    print(f"--|---|--")
    print(f"3 | 4 | 5")
    print(f"--|---|--")
    print(f"6 | 7 | 8")
    pass

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while True:
        printBoard(xState, yState)
        if turn==1:
            print("X's Chance")
            value = int(input("Plase enter a value: "))
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input("Plase enter a value: "))
            yState[value] = 1
        break; 