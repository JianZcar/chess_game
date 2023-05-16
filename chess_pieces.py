import pygame as pg


class ChessPiece:
    def __init__(self, color: int, piece_type: int, location: tuple):
        self.color = color
        self.piece_type = piece_type
        self.location = location

    def __str__(self):
        return f"{self.color} {self.piece_type} at {self.location}"

    def moves(self):
        match self.piece_type:
            case 0:
                # King
                return [(self.location[0] + 1, self.location[1] + 1),
                        (self.location[0] + 1, self.location[1] - 1),
                        (self.location[0] - 1, self.location[1] + 1),
                        (self.location[0] - 1, self.location[1] - 1),
                        (self.location[0] + 1, self.location[1]),
                        (self.location[0] - 1, self.location[1]),
                        (self.location[0], self.location[1] + 1),
                        (self.location[0], self.location[1] - 1)]
            case 1:
                # Queen
                return [(self.location[0] + i, self.location[1] + i) for i in range(1, 8)] + \
                       [(self.location[0] - i, self.location[1] - i) for i in range(1, 8)] + \
                       [(self.location[0] + i, self.location[1] - i) for i in range(1, 8)] + \
                       [(self.location[0] - i, self.location[1] + i) for i in range(1, 8)] + \
                       [(self.location[0] + i, self.location[1]) for i in range(1, 8)] + \
                       [(self.location[0] - i, self.location[1]) for i in range(1, 8)] + \
                       [(self.location[0], self.location[1] + i) for i in range(1, 8)] + \
                       [(self.location[0], self.location[1] - i) for i in range(1, 8)]

            case 2:
                # Bishop
                return [(self.location[0] + i, self.location[1] + i) for i in range(1, 8)] + \
                       [(self.location[0] - i, self.location[1] - i) for i in range(1, 8)] + \
                       [(self.location[0] + i, self.location[1] - i) for i in range(1, 8)] + \
                       [(self.location[0] - i, self.location[1] + i) for i in range(1, 8)]

            case 3:
                # Knight
                return [(self.location[0] + 2, self.location[1] + 1),
                        (self.location[0] + 2, self.location[1] - 1),
                        (self.location[0] - 2, self.location[1] + 1),
                        (self.location[0] - 2, self.location[1] - 1),
                        (self.location[0] + 1, self.location[1] + 2),
                        (self.location[0] + 1, self.location[1] - 2),
                        (self.location[0] - 1, self.location[1] + 2),
                        (self.location[0] - 1, self.location[1] - 2)]

            case 4:
                # Rook
                return [(self.location[0] + i, self.location[1]) for i in range(1, 8)] + \
                       [(self.location[0] - i, self.location[1]) for i in range(1, 8)] + \
                       [(self.location[0], self.location[1] + i) for i in range(1, 8)] + \
                       [(self.location[0], self.location[1] - i) for i in range(1, 8)]

    def sprite(self):
        chess_pieces = pg.image.load("chess_pieces.png")
        cropped_region = (286 * self.piece_type, 286 * self.color, 286, 286)
        chess_piece = pg.Surface.subsurface(chess_pieces, cropped_region)
        chess_piece = pg.transform.scale(chess_piece, (80, 80))
        return chess_piece

    def draw(self, screen=pg.display.set_mode((1280, 720)),
             square_size: int = 80, border_thickness: int = 40):
        p = 6 if self.color == 0 else 0
        screen.blit(self.sprite(), (self.location[0] * square_size + border_thickness,
                                    ((7 - self.location[1]) * square_size + border_thickness + p)))
