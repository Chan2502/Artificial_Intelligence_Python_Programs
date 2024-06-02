def PrintBoard():
    print(f"0 | 1 | 2")
    print(f"--|---|--")
    print(f"3 | 4 | 5")
    print(f"--|---|--")
    print(f"6 | 7 | 8")
    pass

if __name__ == "__tictactoe3__": 
    xState = [0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0]
    turn = 1 
    print("Let's Play Tic Tac Toe")
    print("Player 1 Chance")
    PrintBoard()