import pygame as pg
import chess_board as cb

pg.init()
pg.font.init()
font = pg.font.SysFont('Consolas', 30)
SCREEN_HEIGHT = 1280
SCREEN_WIDTH = 720
screen = pg.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pg.display.set_caption("Chess")
clock = pg.time.Clock()


class Piece:
    def __init__(self, color: str, piece_type: str, location: tuple):
        self.color = color
        self.piece_type = piece_type
        self.location = location
        self.image = pg.image.load(f"images/{self.color}_{self.piece_type}.png")
        self.image = pg.transform.scale(self.image, (80, 80))

    def draw(self):
        screen.blit(self.image, self.location)


def fps_cap(fps: int = 60, time=clock):
    time.tick(fps)


chess_pieces = pg.image.load("chess_pieces.png")
cropped_region = (320 * 0, 320 * 0, 290, 290)
chess_piece = pg.Surface.subsurface(chess_pieces, cropped_region)
chess_piece = pg.transform.scale(chess_piece, (80, 80))


running = True
while running:
    # Game loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    cb.chess_board(screen=screen)
    screen.blit(chess_piece, (0, 0))
    pg.display.update()
    pass

pg.quit()
