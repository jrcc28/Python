import numpy as np

from piece import Piece

# fichas
# tablero - done
# logica


class Chess:
    board = None

    ###
    # Constructor
    ###
    def __init__(self):
        self.start_board()

    ###
    # Create the board for the chess game
    ###
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

        # self.print_board()

    ###
    # Return the board of the game
    ###
    def get_board(self):
        return self.board

    ###
    # Print the board in console
    ###
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

    ###
    # Return the possible moves of the bishop given a row, col position
    ###
    def get_bishop_moves(self, row, col):
        valid_moves = []

        for i in range(1, 8):
            # Check the diagonal going up and to the right
            if (row - i >= 0 and col + i <= 7):
                if (self.board[row - i][col + i] == None):
                    valid_moves.append((row - i, col + i))
                elif (self.board[row - i][col + i].color != self.board[row][col].color):
                    valid_moves.append((row - i, col + i))
                    break
                else:
                    break

        for i in range(1, 8):
            # Check the diagonal going up and to the left
            if (row - i >= 0 and col - i >= 0):
                if (self.board[row - i][col - i] == None):
                    valid_moves.append((row - i, col - i))
                elif (self.board[row - i][col - i].color != self.board[row][col].color):
                    valid_moves.append((row - i, col - i))
                    break
                else:
                    break

        for i in range(1, 8):
            # Check the diagonal going down and to the right
            if (row + i <= 7 and col + i <= 7):
                if (self.board[row + i][col + i] == None):
                    valid_moves.append((row + i, col + i))
                elif (self.board[row + i][col + i].color != self.board[row][col].color):
                    valid_moves.append((row + i, col + i))
                    break
                else:
                    break

        for i in range(1, 8):
            # Check the diagonal going down and to the left
            if (row + i <= 7 and col - i >= 0):
                if (self.board[row + i][col - i] == None):
                    valid_moves.append((row + i, col - i))
                elif (self.board[row + i][col - i].color != self.board[row][col].color):
                    valid_moves.append((row + i, col - i))
                    break
                else:
                    break
        return valid_moves

    ###
    # Return the possible moves of the pawn given a row, col position
    ###
    def get_pawn_moves(self, color, row, col):
        valid_moves = []
        x = 1  # variable to def direction of the pieces
        # Define the moves for each piece
        move = (1, 0)

        if (color == 'w'):
            x = -1

        new_row = row + (move[0]*x)
        new_col = col + (move[1]*x)

        if (not (new_row < 0 or new_row > 7 or new_col < 0 or new_col > 7)):
            if (self.board[new_row][new_col] == None):
                valid_moves.append((new_row, new_col))

            if (row == 1 or row == 6):
                valid_moves = []
                if (self.board[row + (move[0]*x)][col] == None):
                    valid_moves.append((row + (move[0]*x), col))
                    if (self.board[row + (move[0]*x)+x][col] == None):
                        valid_moves.append((row + (move[0]*x) + x, col))

        print(f'valid moves {valid_moves}')
        return valid_moves

    ###
    # Define a function to generate all possible moves for the king and knight on a given position
    ###
    def get_moves(self, piece, color, row, col):
        valid_moves = []
        x = 1  # variable to def direction of the pieces
        # Define the moves for each piece
        moves = {
            'knight': [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)],
            'king': [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)],
        }

        if (color == 'w'):
            x = -1

        for move in moves[piece]:
            new_row = row + (move[0]*x)
            new_col = col + (move[1]*x)
            if (new_row < 0 or new_row > 7 or new_col < 0 or new_col > 7):
                continue
            if (self.board[new_row][new_col] == None):
                valid_moves.append((new_row, new_col))
            elif (self.board[new_row][new_col].color != self.board[row][col].color):
                valid_moves.append((new_row, new_col))

        if (piece == "pawn" and (row == 1 or row == 6)):
            valid_moves = []
            valid_moves.append((row + (move[0]*x), col))
            valid_moves.append((row + (move[0]*x) + x, col))

        return valid_moves

    ###
    # Return the possible moves of the rook given a row, col position
    ###
    def get_rook_moves(self, row, col):
        valid_moves = []
        # Check moves going up
        for i in range(row-1, -1, -1):
            if (self.board[i][col] == None):
                valid_moves.append((i, col))
            elif (self.board[i][col].color != self.board[row][col].color):
                valid_moves.append((i, col))
                break
            else:
                break
        # Check moves going down
        for i in range(row+1, 8):
            if (self.board[i][col] == None):
                valid_moves.append((i, col))
            elif (self.board[i][col].color != self.board[row][col].color):
                valid_moves.append((i, col))
                break
            else:
                break
        # Check moves going left
        for j in range(col-1, -1, -1):
            if (self.board[row][j] == None):
                valid_moves.append((row, j))
            elif (self.board[row][j].color != self.board[row][col].color):
                valid_moves.append((row, j))
                break
            else:
                break
        # Check moves going right
        for j in range(col+1, 8):
            if (self.board[row][j] == None):
                valid_moves.append((row, j))
            elif (self.board[row][j].color != self.board[row][col].color):
                valid_moves.append((row, j))
                break
            else:
                break
        return valid_moves

    ###
    # Return the possible moves of the queen given a row, col position
    ###
    def get_queen_moves(self, row, col):
        valid_moves = []
        # Check moves going up
        for r in range(row-1, -1, -1):
            if (self.board[r][col] == None):
                valid_moves.append((r, col))
            elif (self.board[r][col].color != self.board[row][col].color):
                valid_moves.append((r, col))
                break
            else:
                break
        # Check moves going down
        for r in range(row+1, 8):
            if (self.board[r][col] == None):
                valid_moves.append((r, col))
            elif (self.board[r][col].color != self.board[row][col].color):
                valid_moves.append((r, col))
                break
            else:
                break
        # Check moves going left
        for c in range(col-1, -1, -1):
            if (self.board[row][c] == None):
                valid_moves.append((row, c))
            elif (self.board[row][c].color != self.board[row][col].color):
                valid_moves.append((row, c))
                break
            else:
                break
        # Check moves going right
        for c in range(col+1, 8):
            if (self.board[row][c] == None):
                valid_moves.append((row, c))
            elif (self.board[row][c].color != self.board[row][col].color):
                valid_moves.append((row, c))
                break
            else:
                break
        # Check moves going up and to the left
        r, c = row-1, col-1
        while r >= 0 and c >= 0:
            if (self.board[r][c] == None):
                valid_moves.append((r, c))
            elif (self.board[r][c].color != self.board[row][col].color):
                valid_moves.append((r, c))
                break
            else:
                break
            r -= 1
            c -= 1
        # Check moves going up and to the right
        r, c = row-1, col+1
        while r >= 0 and c <= 7:
            if (self.board[r][c] == None):
                valid_moves.append((r, c))
            elif (self.board[r][c].color != self.board[row][col].color):
                valid_moves.append((r, c))
                break
            else:
                break
            r -= 1
            c += 1
        # Check moves going down and to the left
        r, c = row+1, col-1
        while r <= 7 and c >= 0:
            if (self.board[r][c] == None):
                valid_moves.append((r, c))
            elif (self.board[r][c].color != self.board[row][col].color):
                valid_moves.append((r, c))
                break
            else:
                break
            r += 1
            c -= 1
        # Check moves going down and to the right
        r, c = row+1, col+1
        while r <= 7 and c <= 7:
            if (self.board[r][c] == None):
                valid_moves.append((r, c))
            elif (self.board[r][c].color != self.board[row][col].color):
                valid_moves.append((r, c))
                break
            else:
                break
            r += 1
            c += 1
        return valid_moves

    ###
    # Move a piece from position origin_row, origin_col to row, col
    ###
    def move_piece(self, origin_row, origin_col, row, col):
        self.board[row][col] = self.board[origin_row][origin_col]
        self.board[origin_row][origin_col] = None
        return 0

    ###
    # Checks if a pawn in position row, col has a possibility to eat another piece
    ###
    def can_pawn_eat(self, row, col, current_player):
        can_eat = []
        direction = 1
        if (self.board[row][col] != None and self.board[row][col].color == 'w'):
            direction = -1

        new_row = row+direction
        if ((col-1) >= 0 and self.board[new_row][col-1] != None and self.board[new_row][col-1].color != current_player):
            if (self.board[new_row][col-1].color != self.board[row][col]):
                can_eat.append((row+direction, col-1))
        if ((col+1) <= 7 and self.board[new_row][col+1] != None and self.board[new_row][col+1].color != current_player):
            if (self.board[new_row][col+1].color != self.board[row][col]):
                can_eat.append((new_row, col+1))

        print(f'can eat {can_eat}')
        return can_eat


# chess = Chess()
# valid = []
# valid.append((2, 4))
# Test the function with a pawn on row 1, column 2
# print(valid)
# print(valid[0] in chess.get_moves("pawn", "b", 1, 4))
