import math

class State:
    DRAW = 0
    OVER = 1

class TicTacBoard:
    def __init__(self):
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = 'X'
    
    def make_move(self, move):
        row, col = move
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def undo(self, move):
        row, col = move
        self.board[row][col] = None
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def get_possible_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    moves.append((i, j))
        return moves
    
    def get_state(self):
        if self.is_board_full() or self.get_winner() is not None:
            return State.OVER
        return State.DRAW
    
    def is_board_full(self):
        for row in self.board:
            if None in row:
                return False
        return True
    
    def get_winner(self):
        # Check rows
        for row in self.board:
            if all(cell == 'X' for cell in row):
                return 'X'
            elif all(cell == 'O' for cell in row):
                return 'O'
        
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == 'X' for row in range(3)):
                return 'X'
            elif all(self.board[row][col] == 'O' for row in range(3)):
                return 'O'
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] is not None:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] is not None:
            return self.board[0][2]
        
        return None

def make_best_move():
    bestScore = -math.inf
    bestMove = None
    for move in ticTacBoard.get_possible_moves():
        ticTacBoard.make_move(move)
        score = minimax(False, aiPlayer, ticTacBoard)
        ticTacBoard.undo(move)
        if score > bestScore:
            bestScore = score
            bestMove = move
        else:
            break
    ticTacBoard.make_move(bestMove)


def minimax(isMaxTurn, maximizerMark, board):
    state = board.get_state()
    if state == State.DRAW:
        return 0
    elif state == State.OVER:
        return 1 if board.get_winner() == maximizerMark else -1

    scores = []
    for move in board.get_possible_moves():
        board.make_move(move)
        scores.append(minimax(not isMaxTurn, maximizerMark, board))
        board.undo(move)

    return max(scores) if isMaxTurn else min(scores)

def print_board(board):
    for row in board:
        print(" " + " | ".join(cell if cell is not None else " " for cell in row))
        print("----+---+----")

# Initialize the Tic Tac Toe board
ticTacBoard = TicTacBoard()

# Set the AI player
aiPlayer = 'X'

# Main game loop
try : 
    for _ in range(9):  
    # Print the Tic Tac Toe board
        print_board(ticTacBoard.board)

    # Player's turn
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        ticTacBoard.make_move((row, col))

    # AI's turn
        make_best_move()
except TypeError:
    print("GAME IS OVER")

# Print the final Tic Tac Toe board
print_board(ticTacBoard.board)
