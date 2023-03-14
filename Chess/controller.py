from game import Chess
from interface import UI

# recibe instrucciones de la interfaz e invoca al modelo game
# tiene opciones para el game
# crea new game
# recibe un mover ficha y valida el tipo de ficha para hacer el llamado de mov al modelo
# llama tablero para darlo a la vista


class Controller:
    def __init__(self):
        self.chess = Chess()
        self.interface = UI(self)
        self.interface.on_execute()

    def get_board(self):
        return self.chess.get_board()

    # def reset_game(self):
    #    self.chess.start_board()


if __name__ == "__main__":
    controller = Controller()
