from game import Chess
from interface import UI

# recibe instrucciones de la interfaz e invoca al modelo game
# tiene opciones para el game
# crea new game
# recibe un mover ficha y valida el tipo de ficha para hacer el llamado de mov al modelo
# llama tablero para darlo a la vista


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
        self.chess = Chess()
        self.interface = UI(self)
        self.interface.on_execute()

    ###
    # Method to get the board of the game
    ###
    def get_board(self):
        return self.chess.get_board()

    ###
    # Checks possible moves for a selected piece
    ###
    def first_move(self, row, col, board):
        self.possible_moves = []
        self.selected_piece_row = row
        self.selected_piece_col = col
        self.selected_piece = True

        match board[row][col].type:
            case "rook":
                print("calling rook moves")
                self.possible_moves = self.chess.get_rook_moves(
                    row, col)
            case "queen":
                print("calling queen moves")
                self.possible_moves = self.chess.get_queen_moves(
                    row, col)
            case "bishop":
                print("calling bishop moves")
                self.possible_moves = self.chess.get_bishop_moves(
                    row, col)
            case "pawn":
                print("calling pawn moves")
                self.possible_moves = self.chess.get_pawn_moves(self.current_player,
                                                                row, col)
            case _:
                print("calling other moves")
                self.possible_moves = self.chess.get_moves(
                    board[row][col].type, board[row][col].color, row, col)

    ###
    # Checks if it is possible the movement of a piece
    ###
    def second_move(self, row, col, board):
        self.selected_piece = False
        if (self.current_player == "w"):
            print("validating white move")
            print((row, col) in self.possible_moves)
            if ((board[row][col] == None or board[row][col].color == "b") and (row, col) in self.possible_moves):
                print("white piece moved")
                self.chess.move_piece(
                    self.selected_piece_row, self.selected_piece_col, row, col)
                self.current_player = "b"
        else:
            print("validating black move")
            if ((board[row][col] == None or board[row][col].color == "w") and (row, col) in self.possible_moves):
                print("black piece moved")
                self.chess.move_piece(
                    self.selected_piece_row, self.selected_piece_col, row, col)
                self.current_player = "w"
        self.possible_moves = []

    ###
    # Checks if it is the first click or the second click to move a piece
    ###
    def select_piece(self, row, col):
        print(f'origin: {self.selected_piece_row}, {self.selected_piece_col}')
        print(f'destiny: {row}, {col}')
        board = self.get_board()

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


if __name__ == "__main__":
    controller = Controller()
