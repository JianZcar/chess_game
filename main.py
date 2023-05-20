import pygame as pg
import chess_board as cb
import chess_pieces as cp
import game_logic as gl

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


def chess_board():
    border = cb.border(80)
    pg.draw.rect(screen, border[1], border[0]), (0, 0)
    for tile in cb.tiles(80, 40):
        pg.draw.rect(screen, tile[1], tile[0])
    for x in cb.chess_coordinates(80, 40):
        screen.blit(x[0][0], x[0][1])
        screen.blit(x[1][0], x[1][1])


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

list_of_pieces = [king, queen, pawn, rook, knight, bishop, b_king, b_queen, b_pawn, b_rook, b_knight, b_bishop]
board_state = gl.board_state()
for piece in list_of_pieces:
    board_state = gl.insert_piece(board_state, piece)
running = True
while running:
    # Game loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    chess_board()
    for y in board_state:
        [screen.blit(piece.draw()[0], piece.draw()[1]) if piece != 0 else None for piece in y]
    pg.display.update()
    pass

pg.quit()
