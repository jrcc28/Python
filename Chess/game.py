import numpy as np

from piece import Piece

# fichas
# tablero - done
# logica


class Chess:
    board = None

    def __init__(self):
        self.start_board()

    def start_board(self):
        # def of pieces in the board
        self.board = np.array([[None] * 8,
                               [None] * 8,
                               [None] * 8,
                               [None] * 8,
                               [None] * 8,
                               [None] * 8,
                               [None] * 8,
                               [None] * 8])
        # Pawns
        # Iterate over each column of the current row
        for j in range(len(self.board[0])):
            # Access the current element of the matrix
            self.board[1][j] = Piece("pawn", "b", 1, j)
            self.board[6][j] = Piece("pawn", "w", 6, j)

        # Bishop
        self.board[0][2] = Piece("bishop", "b", 0, 2)
        self.board[0][5] = Piece("bishop", "b", 0, 5)
        self.board[7][2] = Piece("bishop", "w", 7, 2)
        self.board[7][5] = Piece("bishop", "w", 7, 5)

        # Knight
        self.board[0][1] = Piece("knight", "b", 0, 1)
        self.board[0][6] = Piece("knight", "b", 0, 6)
        self.board[7][1] = Piece("knight", "w", 7, 1)
        self.board[7][6] = Piece("knight", "w", 7, 6)

        # Rook
        self.board[0][0] = Piece("rook", "b", 0, 0)
        self.board[0][7] = Piece("rook", "b", 0, 7)
        self.board[7][0] = Piece("rook", "w", 7, 0)
        self.board[7][7] = Piece("rook", "w", 7, 7)

        # Queen
        self.board[0][3] = Piece("queen", "b", 0, 3)
        self.board[7][3] = Piece("queen", "w", 7, 3)

        # King
        self.board[0][4] = Piece("king", "b", 0, 4)
        self.board[7][4] = Piece("king", "w", 7, 4)

        self.print_board()

    def get_board(self):
        return self.board

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


# chess = Chess()
