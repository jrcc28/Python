import pygame
# pygame
# muestra tablero
# envia pos de mov al controller


class UI:
    def __init__(self, controller):
        self.controller = controller
        self._running = True
        self.screen = None
        self.size = self.weight, self.height = 720, 720
        self.offset_pos_x = 20
        self.offset_pos_y = 20
        self.piece_size = 85
        pygame.init()

    # method to display the screen
    def on_init(self):
        self.screen = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.update_screen(self.controller.get_board(), [])
        self._running = True

    # This method receives a board and update the screen according to the board
    def update_screen(self, board, possible_moves):
        # board
        imp = pygame.image.load(
            "img/board.jpg").convert()
        self.screen.blit(imp, (0, 0))

        # Update screen with pieces
        for i in range(len(board)):
            # Iterate over each column of the current row
            for j in range(len(board[i])):
                # Access the current element of the matrix
                if (board[i][j] != None):
                    # Load the piece image
                    piece_image = pygame.image.load(
                        "img/"+board[i][j].color + "_" + board[i][j].type + ".png")

                    # Set the position of the piece
                    piece_position = (self.offset_pos_x+(self.piece_size*j),
                                      self.offset_pos_y+(self.piece_size*i))
                    self.screen.blit(piece_image, piece_position)

        # Update the display
        self.update_screen_possible_moves(possible_moves)
        pygame.display.update()

    def update_screen_possible_moves(self, possible_moves):
        # Update screen with possible moves
        for move in (possible_moves):
            # Load the piece image
            piece_image = pygame.image.load(
                "img/dot.png")
            # Set the position of the piece
            piece_position = (self.offset_pos_x+28+(self.piece_size*int(move[1])),
                              self.offset_pos_y+28+(self.piece_size*int(move[0])))
            self.screen.blit(piece_image, piece_position)

        # Update the display
        # pygame.display.update()

    ###
    #  def of events in screen
    ###

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            board = self.controller.get_board()
            possible_moves = []
            pos = pygame.mouse.get_pos()
            btn = pygame.mouse
            print("col = {} board: {}, row = {}  board: {}, btn: {}".format(
                pos[0], (pos[0]-self.offset_pos_x)//85, pos[1], (pos[1]-self.offset_pos_y)//85, btn.get_pressed()))
            if ((pos[0]-self.offset_pos_x)//85 >= 0 and (pos[0]-self.offset_pos_x)//85 <= 7 and (pos[1]-self.offset_pos_x)//85 >= 0 and (pos[1]-self.offset_pos_x)//85 <= 7):
                possible_moves = self.controller.select_piece(
                    ((pos[1]-self.offset_pos_y)//85), (pos[0]-self.offset_pos_x)//85)
                # on pressed call the controller to update the view with possible moves
                # self.update_screen_possible_moves(possible_moves)

            self.update_screen(board, possible_moves)

            # Method to clean up modules of pygame
    def on_cleanup(self):
        pygame.quit()

    # method to execute the screen of the game and read events
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            # self.on_loop()
            # self.on_render()
        self.on_cleanup()
