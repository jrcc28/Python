# Definition of Class Piece
class Piece:
    def __init__(self, type='', color='', pos_x=0, pos_y=0):
        self.type = type
        self.color = color
        self.x = pos_x
        self.y = pos_y

    def set_attr(self, type, color, pos_x, pos_y):
        self.type = type
        self.color = color
        self.x = pos_x
        self.y = pos_y

    def get_type(self):
        return self.type

    def get_color(self):
        return self.color

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return self.type
