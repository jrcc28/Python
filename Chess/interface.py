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
        self.fixed_pos_x = 20
        self.fixed_pos_y = 20
        self.piece_size = 85
        pygame.init()

    # method to display the screen
    def on_init(self):
        self.screen = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.put_images_on_screen(self.controller.get_board())
        self._running = True

    # This method receives a board and update the screen according to the board
    def put_images_on_screen(self, board):
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
                    piece_position = (self.fixed_pos_x+(self.piece_size*j),
                                      self.fixed_pos_y+(self.piece_size*i))
                    self.screen.blit(piece_image, piece_position)

        # Update the display
        pygame.display.update()

    # def of events in screen
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            btn = pygame.mouse
            print("x = {} board: {}, y = {}  board: {}, btn: {}".format(
                pos[0], pos[0]//85, pos[1], pos[1]//85, btn.get_pressed()))

            # on pressed call the controller to update the view with possible moves

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
