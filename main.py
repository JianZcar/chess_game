import pygame as pg
import chess_board as cb
import chess_pieces as cp

pg.init()
pg.font.init()
font = pg.font.SysFont('Consolas', 30)
SCREEN_HEIGHT = 1280
SCREEN_WIDTH = 720
pg.display.set_icon(cp.game_icon())
screen = pg.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pg.display.set_caption("Chess")
clock = pg.time.Clock()


def fps_cap(fps: int = 60, time=clock):
    time.tick(fps)


king = cp.ChessPiece(color=0, piece_type=0, location=(0, 0))
queen = cp.ChessPiece(color=0, piece_type=1, location=(1, 0))
pawn = cp.ChessPiece(color=0, piece_type=5, location=(2, 0))
rook = cp.ChessPiece(color=0, piece_type=2, location=(3, 0))
knight = cp.ChessPiece(color=0, piece_type=3, location=(4, 0))
bishop = cp.ChessPiece(color=0, piece_type=4, location=(5, 0))

b_king = cp.ChessPiece(color=1, piece_type=0, location=(0, 7))
b_queen = cp.ChessPiece(color=1, piece_type=1, location=(1, 7))
b_pawn = cp.ChessPiece(color=1, piece_type=5, location=(2, 7))
b_rook = cp.ChessPiece(color=1, piece_type=2, location=(3, 7))
b_knight = cp.ChessPiece(color=1, piece_type=3, location=(4, 7))
b_bishop = cp.ChessPiece(color=1, piece_type=4, location=(5, 7))

running = True
while running:
    # Game loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    cb.chess_board(screen=screen)
    king.draw(screen=screen)
    queen.draw(screen=screen)
    pawn.draw(screen=screen)
    rook.draw(screen=screen)
    knight.draw(screen=screen)
    bishop.draw(screen=screen)

    b_king.draw(screen=screen)
    b_queen.draw(screen=screen)
    b_pawn.draw(screen=screen)
    b_rook.draw(screen=screen)
    b_knight.draw(screen=screen)
    b_bishop.draw(screen=screen)
    pg.display.update()
    pass

pg.quit()
