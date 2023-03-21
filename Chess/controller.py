from game import Chess
from interface import UI


class Controller:

    ###
    # Constructor of class Controller
    ###
    def __init__(self):
        self.selected_piece_row = -1
        self.selected_piece_col = -1
        self.current_player = "w"
        self.possible_moves = []
        self.selected_piece = False
        self.checkmate = False
        self.winner = ''
        self.check = False
        self.king_in_danger = (-1, -1)
        self.attacker = (-1, -1)
        self.tables = False
        self.chess = Chess()
        self.interface = UI(self)
        self.interface.on_execute()

    ###
    # Method to get the board of the game
    ###
    def get_board(self):
        return self.chess.get_board()

    ###
    # Returns the data of a check in the board
    ###
    def get_check_data(self):
        return self.check, self.king_in_danger, self.attacker

    ###
    # Checks possible moves for a selected piece
    ###
    def first_move(self, row, col, board):
        self.possible_moves = []
        self.selected_piece_row = row
        self.selected_piece_col = col
        self.selected_piece = True

        self.possible_moves = self.chess.get_moves_for_one_piece(
            board[row][col].type, row, col, board[row][col].color)

    ###
    # Checks if it is possible the movement of a piece
    ###
    def second_move(self, row, col, board):
        self.selected_piece = False
        if (self.current_player == "w"):
            if ((board[row][col] == None or board[row][col].color == "b") and (row, col) in self.possible_moves):
                print("white piece moved")
                self.chess.move_piece(
                    self.selected_piece_row, self.selected_piece_col, row, col)
                self.current_player = "b"
        else:
            if ((board[row][col] == None or board[row][col].color == "w") and (row, col) in self.possible_moves):
                print("black piece moved")
                self.chess.move_piece(
                    self.selected_piece_row, self.selected_piece_col, row, col)
                self.current_player = "w"

        # Verify a check
        self.check, self.king_in_danger, self.attacker = self.chess.is_check(
            board, "w")
        if (not self.check):
            self.check, self.king_in_danger, self.attacker = self.chess.is_check(
                board, "b")

        # Check the board for a checkmate
        if (self.current_player == 'w'):
            self.checkmate = self.chess.is_checkmate("b")
        else:
            self.checkmate = self.chess.is_checkmate("w")

        if (self.checkmate):
            if (self.current_player == 'w'):
                self.winner = "Black"
            else:
                self.winner = 'White'

        self.tables = self.chess.is_stalemate(
            'w') or self.chess.is_stalemate('b')

        if (self.tables):
            self.checkmate = True

        self.possible_moves = []

    ###
    # Checks if it is the first click or the second click to move a piece
    ###
    def select_piece(self, row, col):
        # print(f'origin: {self.selected_piece_row}, {self.selected_piece_col}')
        # print(f'destiny: {row}, {col}')

        if (self.checkmate):
            print('There is a winner')
            return []

        board = self.get_board()

        # move in case of castling
        if ((row, col) in self.possible_moves
            and board[row][col] != None
            and board[row][col].type == 'rook'
            and board[self.selected_piece_row][self.selected_piece_col] != None
                and board[self.selected_piece_row][self.selected_piece_col].type == 'king'):
            self.chess.move_piece(
                self.selected_piece_row, self.selected_piece_col, row, col)
            if (self.current_player == 'w'):
                self.current_player = "b"
            else:
                self.current_player = "w"
            self.selected_piece = False

            return []

        # Another piece was selected, the var selected_piece will be reset
        if (self.selected_piece and board[row][col] != None and board[row][col].color == self.current_player):
            self.selected_piece = False
        # Check if it is the second move
        if (self.selected_piece and (board[row][col] == None or board[self.selected_piece_row][self.selected_piece_col].color == self.current_player)):
            self.second_move(row, col, board)
        else:  # It is the first move
            if (board[row][col] != None and board[row, col].color != self.current_player):
                return []
            if (board[row][col] != None and board[row][col].color == self.current_player):
                self.first_move(row, col, board)
            # check if the selected piece is pawn, so we need to check if there are pieces to eat
            if (board[row][col] != None and board[row, col].type == "pawn"):
                for move in self.chess.can_pawn_eat(row, col, self.current_player):
                    self.possible_moves.append(move)

        print(self.possible_moves)
        return self.possible_moves

    def restart(self):
        del self.chess
        self.chess = Chess()
        self.selected_piece_row = -1
        self.selected_piece_col = -1
        self.current_player = "w"
        self.possible_moves = []
        self.selected_piece = False
        self.checkmate = False
        self.winner = ''
        self.check = False
        self.tables = False
        self.king_in_danger = (-1, -1)
        self.attacker = (-1, -1)


if __name__ == "__main__":
    controller = Controller()
