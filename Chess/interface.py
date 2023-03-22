import pygame

# muestra tablero
# envia pos de mov al controller


class UI:

    ###
    # Constructor for class UI
    ###
    def __init__(self, controller):
        self.controller = controller
        self._running = True
        self.screen = None
        self.size = self.weight, self.height = 1080, 720
        self.need_option = False
        self.offset_pos_x = 20
        self.offset_pos_y = 20
        self.piece_size = 85
        self.dot_size = 25
        self.color_text = pygame.Color("White")
        pygame.init()

    ###
    #  Method to display the screen
    ###
    def on_init(self):
        pygame.display.set_caption('Chess Game')
        self.screen = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.update_screen(self.controller.get_board(), [])
        self._running = True

    ###
    #  This method receives a board and possible moves for a piece that was selected and update the screen according to the data
    ###
    def update_screen(self, board, possible_moves):
        # print(pygame.font.get_fonts())
        font = pygame.font.Font('freesansbold.ttf', 20)
        self.screen.fill(pygame.Color("Black"))

        player = 'white'
        if (self.controller.current_player == 'b'):
            player = 'black'

        text = font.render(
            'Current player: ' + player, False, self.color_text)
        self.screen.blit(text, (730, 10))

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

        # Update screen in case that a pawn can be converted
        self.show_convert_pawn_options()

        # Update screen in case of check
        self.update_screen_check()

        # Update the display
        self.update_screen_possible_moves(possible_moves)
        pygame.display.update()

    ###
    # Update the screen if there is a check in the board
    ###
    def update_screen_check(self):
        check, king_pos, attacker_pos = self.controller.get_check_data()
        if (check):
            font = pygame.font.Font('freesansbold.ttf', 20)

            player = 'white'
            if (self.controller.current_player == 'b'):
                player = 'black'

            text = font.render(
                'Watch out!', False, self.color_text)
            self.screen.blit(text, (740, 360))

            text = font.render('The ' + player +
                               ' king is under attack!', False, self.color_text)
            self.screen.blit(text, (740, 385))

            # Load the piece image
            piece_image = pygame.image.load(
                "img/check_dot.png")
            # Set the dot on the position of the king in danger
            piece_position = (self.offset_pos_x+self.dot_size+(self.piece_size*king_pos[1]),
                              self.offset_pos_y+self.dot_size+(self.piece_size*king_pos[0]))
            self.screen.blit(piece_image, piece_position)

            # Set the dot on the position of the attacker
            piece_position = (self.offset_pos_x+self.dot_size+(self.piece_size*attacker_pos[1]),
                              self.offset_pos_y+self.dot_size+(self.piece_size*attacker_pos[0]))
            self.screen.blit(piece_image, piece_position)

    ###
    # Update the screen adding a guide for possible moves for a piece
    ###
    def update_screen_possible_moves(self, possible_moves):
        # Update screen with possible moves
        for move in (possible_moves):
            # Load the piece image
            piece_image = pygame.image.load(
                "img/dot.png")
            # Set the position of the piece
            piece_position = (self.offset_pos_x+self.dot_size+(self.piece_size*int(move[1])),
                              self.offset_pos_y+self.dot_size+(self.piece_size*int(move[0])))
            self.screen.blit(piece_image, piece_position)

    def show_checkmate(self):
        self.screen.fill(pygame.Color("Black"))
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render(
            'Checkmate!', False, self.color_text)
        self.screen.blit(text, (425, 260))

        text = font.render(self.controller.winner +
                           ' Wins!', False, self.color_text)
        self.screen.blit(text, (430, 300))

        text = font.render(
            'Press any key to start a new game!', False, self.color_text)
        self.screen.blit(text, (300, 400))

        pygame.display.update()

    def show_tables(self):
        self.screen.fill(pygame.Color("Black"))
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render(
            'It is a tie!', False, self.color_text)
        self.screen.blit(text, (425, 260))

        text = font.render(
            'Press any key to start a new game!', False, self.color_text)
        self.screen.blit(text, (300, 400))

        pygame.display.update()

    ###
    #  def of events received from screen
    ###
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            board = self.controller.get_board()
            possible_moves = []
            pos = pygame.mouse.get_pos()
            btn = pygame.mouse
            pos_col = (pos[0]-self.offset_pos_x)//85
            pos_row = (pos[1]-self.offset_pos_y)//85
            print("col = {} board: {}, row = {}  board: {}, btn: {}".format(
                pos[0], (pos[0]-self.offset_pos_x)//85, pos[1], (pos[1]-self.offset_pos_y)//85, btn.get_pressed()))
            if (pos_col >= 0
                and pos_col <= 7
                and pos_row >= 0
                    and pos_row <= 7):
                possible_moves = self.controller.select_piece(
                    pos_row, pos_col)

            if (not self.controller.checkmate and not self.controller.tables):
                self.update_screen(board, possible_moves)

                if (self.need_option):
                    self.wait_for_option(pos_row, pos_col)

            elif (self.controller.tables):
                self.show_tables()
            elif (self.controller.checkmate):
                self.show_checkmate()

        if event.type == pygame.KEYDOWN:
            if (self.controller.checkmate and self.controller.tables):
                self.controller.restart()
                self.update_screen(self.controller.get_board(), [])

    def show_convert_pawn_options(self):
        if (self.controller.convert_pawn):
            # self.controller.convert_pawn_to()
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = "Pawn can be converted!\nSelect an option by\nentering the corresponding\nnumber:\n1.Queen\n2.Knight\n3.bishop\n4.rook"
            lines = text.splitlines()
            for i, l in enumerate(lines):
                text_to_show = font.render(l, False, self.color_text)
                self.screen.blit(text_to_show, (740, 300 + 25*i))

            self.need_option = True

    def wait_for_option(self, pos_row, pos_col):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_1 or event.key == pygame.K_KP1):
                    self.controller.convert_pawn_to(1, pos_row, pos_col)
                    self.need_option = False
                    break

                if (event.key == pygame.K_2 or event.key == pygame.K_KP2):
                    self.controller.convert_pawn_to(2, pos_row, pos_col)
                    self.need_option = False
                    break

                if (event.key == pygame.K_3 or event.key == pygame.K_KP3):
                    self.controller.convert_pawn_to(3, pos_row, pos_col)
                    self.need_option = False
                    break

                if (event.key == pygame.K_4 or event.key == pygame.K_KP4):
                    self.controller.convert_pawn_to(4, pos_row, pos_col)
                    self.need_option = False
                    break

        self.update_screen(self.controller.get_board(), [])

    ###
    #  Method to clean up modules of pygame
    ###

    def on_cleanup(self):
        pygame.quit()

    ###
    #  method to execute the screen of the game and read events
    ###
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
        self.on_cleanup()
