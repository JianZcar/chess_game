import pygame as pg
pg.font.init()


def border(square_size: int, color=pg.Color(255, 234, 230), border_thickness: int = 40) -> (pg.Rect, pg.Color):
    board = square_size * 8
    border_ = pg.Rect(0, 0, board + (border_thickness * 2), board + (border_thickness * 2))
    return border_, color


def tiles(square_size: int, screen_location: int, w_color=pg.Color("white"),
          b_color=pg.Color("gray")) -> (pg.Rect, pg.Color):
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = w_color
            else:
                color = b_color
            tile = pg.Rect(col * square_size + screen_location,
                           row * square_size + screen_location, square_size, square_size)
            yield tile, color


def chess_coordinates(square_size: int, border_thickness,
                      font=pg.font.SysFont('Consolas', 30)) -> (pg.Surface, pg.Surface):
    x = "ABCDEFGH"
    y = "12345678"[::-1]
    for i in range(8):
        text1 = font.render(x[i], False, (0, 0, 0))
        text2 = font.render(y[i], False, (0, 0, 0))
        yield ((text1, ((border_thickness + (i * square_size) + (square_size / 2) - 10,
                        border_thickness + (square_size * 8) + 5))),
               (text2, ((border_thickness / 2) - 5,
                        border_thickness + (i * square_size) + (square_size / 2) - 10)))
