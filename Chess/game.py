import numpy as np

from piece import Piece

# fichas
# tablero
# logica


class Chess:
    def __init__(self):
        self.board = np.array([[None] * 8,
                               [None] * 8,
                               [None] * 8,
                               [None] * 8,
                               [None] * 8,
                               [None] * 8,
                               [None] * 8,
                               [None] * 8])
        self.start_board()

    def start_board(self):
        # def of pieces in the board
        # Pawns
        # Iterate over each column of the current row
        for j in range(len(self.board[0])):
            # Access the current element of the matrix
            self.board[1][j] = Piece("Pawn", "B", 1, j)
            self.board[6][j] = Piece("Pawn", "W", 6, j)

        # Bishop
        self.board[0][2] = Piece("Bishop", "B", 0, 2)
        self.board[0][5] = Piece("Bishop", "B", 0, 5)
        self.board[7][2] = Piece("Bishop", "W", 7, 2)
        self.board[7][5] = Piece("Bishop", "W", 7, 5)

        # Knight
        self.board[0][1] = Piece("Knight", "B", 0, 1)
        self.board[0][6] = Piece("Knight", "B", 0, 6)
        self.board[7][1] = Piece("Knight", "W", 7, 1)
        self.board[7][6] = Piece("Knight", "W", 7, 6)

        # Rook
        self.board[0][0] = Piece("Rook", "B", 0, 0)
        self.board[0][7] = Piece("Rook", "B", 0, 7)
        self.board[7][0] = Piece("Rook", "W", 7, 0)
        self.board[7][7] = Piece("Rook", "W", 7, 7)

        # Queen
        self.board[0][3] = Piece("Queen", "B", 0, 3)
        self.board[7][3] = Piece("Queen", "W", 7, 3)

        # King
        self.board[0][4] = Piece("King", "B", 0, 4)
        self.board[7][4] = Piece("King", "W", 7, 4)

        self.print_board()

    def print_board(self):
        for i in range(len(self.board)):
            # Iterate over each column of the current row
            for j in range(len(self.board[i])):
                # Access the current element of the matrix
                if (self.board[i][j] != None):
                    print(self.board[i][j].type, end=" ")
                else:
                    print('  .  ', end=" ")
            print()


chess = Chess()
