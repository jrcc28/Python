import copy

from piece import Piece


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
        self.board = ([[None] * 8,
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
    def print_board(self, board):
        for i in range(len(board)):
            # Iterate over each column of the current row
            for j in range(len(board[i])):
                # Access the current element of the matrix
                if (board[i][j] != None):
                    print(board[i][j].type, end=" ")
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

        color = self.board[row][col].color
        moves_to_check = valid_moves
        valid_moves = []
        for move in moves_to_check:
            new_board = self.simulate_move(row, col, move[0], move[1])
            is_check = self.is_check(new_board, color)[0]
            if (not is_check):
                valid_moves.append(move)

        return valid_moves

    ###
    # Return the possible moves of the pawn given a row, col position
    ###
    def get_pawn_moves(self, color, row, col, check=False):
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

        color = self.board[row][col].color
        moves_to_check = valid_moves
        valid_moves = []
        for move in moves_to_check:
            new_board = self.simulate_move(row, col, move[0], move[1])
            is_check = self.is_check(new_board, color)[0]
            if (not is_check):
                valid_moves.append(move)

        if (check):
            valid_moves = self.can_pawn_eat(row, col, color)

        return valid_moves

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

        return can_eat

    ###
    # can a pawn eat a move from king
    ###
    def can_pawn_eat_king(self, row, col):
        can_eat = []
        direction = 1
        if (self.board[row][col] != None and self.board[row][col].color == 'w'):
            direction = -1

        if ((col-1) >= 0):
            can_eat.append((row+direction, col-1))

        if ((col+1) <= 7):
            can_eat.append((row+direction, col+1))

        color = self.board[row][col].color
        moves_to_check = can_eat
        can_eat = []
        for move in moves_to_check:
            new_board = self.simulate_move(row, col, move[0], move[1])
            is_check = self.is_check(new_board, color)[0]
            if (not is_check):
                can_eat.append(move)

        return can_eat

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

        if (piece == "king"):
            if (color == 'w'):
                all_enemy_moves = self.get_enemy_moves('b')
            else:
                all_enemy_moves = self.get_enemy_moves('w')

            # Check for possible positions in which a pawn can eat the king
            [all_enemy_moves.append(x)
             for x in self.can_pawn_eat_king(row, col)]

            valid_moves_king = valid_moves
            valid_moves = []
            [valid_moves.append(elem)
             for elem in valid_moves_king if elem not in all_enemy_moves]
        else:
            color = self.board[row][col].color
            moves_to_check = valid_moves
            valid_moves = []
            for move in moves_to_check:
                new_board = self.simulate_move(row, col, move[0], move[1])
                is_check = self.is_check(new_board, color)[0]
                if (not is_check):
                    valid_moves.append(move)

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

        color = self.board[row][col].color
        moves_to_check = valid_moves
        valid_moves = []
        for move in moves_to_check:
            new_board = self.simulate_move(row, col, move[0], move[1])
            is_check = self.is_check(new_board, color)[0]
            if (not is_check):
                valid_moves.append(move)

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

        color = self.board[row][col].color
        moves_to_check = valid_moves
        valid_moves = []
        for move in moves_to_check:
            new_board = self.simulate_move(row, col, move[0], move[1])
            is_check = self.is_check(new_board, color)[0]
            if (not is_check):
                valid_moves.append(move)

        return valid_moves

    ###
    # Move a piece from position origin_row, origin_col to row, col
    ###
    def move_piece(self, origin_row, origin_col, row, col):
        self.board[row][col] = self.board[origin_row][origin_col]
        self.board[origin_row][origin_col] = None
        return 0

    ###
    #  Find the king of a given color on the board
    ###
    def find_king(self, color):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != None and self.board[i][j].color == color and self.board[i][j].type == 'king':
                    return (i, j)

    ###
    # Verify is there is a check in the board
    ###
    def is_check(self, board, color):
        # Find the king of the given color on the board
        king_pos = self.find_king(color)

        # Check for attacks from pawns
        if (king_pos != None and (king_pos[0]-1) >= 0 and (king_pos[0]+1) <= 7 and (king_pos[1]-1) >= 0 and (king_pos[1]+1) <= 7
            and board[king_pos[0]-1][king_pos[1]-1] != None
            and board[king_pos[0]-1][king_pos[1]+1] != None
            and board[king_pos[0]+1][king_pos[1]-1] != None
                and board[king_pos[0]+1][king_pos[1]+1] != None):
            if color == 'w':
                if king_pos[0] > 0 and king_pos[1] > 0 and board[king_pos[0]-1][king_pos[1]-1].type == 'pawn' and board[king_pos[0]-1][king_pos[1]-1].color == 'b':
                    return True, king_pos, (king_pos[0]-1, king_pos[1]-1)
                if king_pos[0] > 0 and king_pos[1] < 7 and board[king_pos[0]-1][king_pos[1]+1].type == 'pawn' and board[king_pos[0]-1][king_pos[1]+1].color == 'b':
                    return True, king_pos, (king_pos[0]-1, king_pos[1]+1)
            else:
                if king_pos[0] < 7 and king_pos[1] > 0 and board[king_pos[0]+1][king_pos[1]-1].type == 'pawn' and board[king_pos[0]+1][king_pos[1]-1].color == 'w':
                    return True, king_pos, (king_pos[0]+1, king_pos[1]-1)
                if king_pos[0] < 7 and king_pos[1] < 7 and board[king_pos[0]+1][king_pos[1]+1].type == 'pawn' and board[king_pos[0]+1][king_pos[1]-1].color == 'w':
                    return True, king_pos, (king_pos[0]+1, king_pos[1]+1)

        # Check for attacks from knights
        knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                        (-2, -1), (-1, -2), (1, -2), (2, -1)]
        for move in knight_moves:
            row = king_pos[0] + move[0]
            col = king_pos[1] + move[1]
            if row < 0 or row > 7 or col < 0 or col > 7:
                continue
            if board[row][col] != None and board[row][col].color != color and board[row][col].type == 'knight':
                return True, king_pos, (row, col)

        # Check for attacks from rooks and queens
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direction in directions:
            row = king_pos[0] + direction[0]
            col = king_pos[1] + direction[1]
            while row >= 0 and row < 8 and col >= 0 and col < 8:
                if board[row][col] != None:
                    if board[row][col].color == color:
                        break
                    if board[row][col].type == 'rook' or board[row][col].type == 'queen':
                        return True, king_pos, (row, col)
                    else:
                        break
                row += direction[0]
                col += direction[1]

        # Check for attacks from bishops and queens
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction in directions:
            row = king_pos[0] + direction[0]
            col = king_pos[1] + direction[1]
            while row >= 0 and row < 8 and col >= 0 and col < 8:
                if board[row][col] != None:
                    if board[row][col].color == color:
                        break
                    if board[row][col].type == 'bishop' or board[row][col].type == 'queen':
                        return True, king_pos, (row, col)
                    else:
                        break
                row += direction[0]
                col += direction[1]

        # No attacks found, return False
        return (False, (-1, -1), (-1, -1))

    ###
    # Get moves of the pieces of the given color
    # This method doesn't consider king moves
    # Also, it doesn't consider pawns moves
    ###
    def get_enemy_moves(self, color, search_all=False):
        moves = []
        for row in range(8):
            for col in range(8):
                if (self.board[row][col] != None and self.board[row][col].color == color):
                    [moves.append(x) for x in self.get_moves_for_one_piece(
                        self.board[row][col].type, row, col, color, search_all)]

        # Return a list of possible moves without duplicate values
        return list(set(moves))

    ###
    # Get moves of the piece given in parameter
    # search_king indicates that we will look for moves of the king, in other case that it is false
    # we will look only for moves of the knight.
    ###
    def get_moves_for_one_piece(self, type, row, col, color, search_king=True):
        moves = []
        match type:
            case "rook":
                [moves.append(x) for x in self.get_rook_moves(
                    row, col)]
            case "queen":
                [moves.append(x) for x in self.get_queen_moves(
                    row, col)]
            case "bishop":
                [moves.append(x) for x in self.get_bishop_moves(
                    row, col)]
            case "pawn":
                if (search_king):
                    [moves.append(x) for x in self.get_pawn_moves(
                        color, row, col)]
            case _:
                if (search_king):
                    [moves.append(x) for x in self.get_moves(
                        self.board[row][col].type, color, row, col)]
                else:
                    [moves.append(x) for x in self.get_moves(
                        "knight", color, row, col)]
        return moves

    ###
    # Check if the king of the given color is in checkmate
    ###
    def is_checkmate(self, color):
        # Check if the king is in check
        if not self.is_check(self.board, color)[0]:
            # print('It is not a check')
            return False

        pos = self.find_king(color)
        king_moves = self.get_moves('king', color, pos[0], pos[1])

        # Check if the king can escape check
        if (len(king_moves) > 0):
            print(f'black king_moves {king_moves}')
            return False

        if (color == 'w'):
            attacking_color = 'b'
        else:
            attacking_color = 'w'

        # for piece in board:
        for row in range(8):
            for col in range(8):
                if (self.board[row][col] == None):
                    continue
                if (self.board[row][col].color == attacking_color):
                    continue
                moves = self.get_moves_for_one_piece(
                    self.board[row][col].type, row, col, color, False)
                print(self.board[row][col].type)
                if (self.board[row][col] != None and self.board[row][col] == 'pawn'):
                    [moves.append(x) for x in self.get_pawn_moves(
                        color, row, col)]
                print(moves)
                for move in moves:
                    new_board = self.simulate_move(row, col, move[0], move[1])
                    if not self.is_check(new_board, color)[0]:
                        print(
                            f'There are possible moves or blocks {row}{col} to {move}')
                        return False

        # If none of the above conditions are met, it's checkmate
        return True

    ###
    # Simulate a move of a piece on the board
    ###
    def simulate_move(self, origin_row, origin_col, row, col):
        simulated_board = copy.deepcopy(self.board)
        simulated_board[row][col] = simulated_board[origin_row][origin_col]
        simulated_board[origin_row][origin_col] = None
        return simulated_board


# chess = Chess()
# print(chess.get_enemy_moves('b', True))
# print(chess.get_enemy_moves('w', True))

# chess.move_piece(6, 4, 4, 4)
# chess.move_piece(1, 5, 3, 5)
# chess.move_piece(7, 3, 3, 7)
# chess.move_piece(1, 6, 2, 7)
# chess.print_board(chess.board)
# # chess.move_piece(7, 6, 5, 5)
# # chess.move_piece(0, 3, 3, 6)
# # chess.move_piece(6, 4, 5, 4)
# # chess.move_piece(1, 5, 2, 5)
# # chess.move_piece(7, 3, 5, 3)
# # chess.move_piece(0, 1, 2, 2)
# # chess.move_piece(5, 3, 5, 0)
# print(chess.is_checkmate('b'))
