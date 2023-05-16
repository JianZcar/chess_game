import pygame as pg
pg.font.init()


def chess_board(square_size: int = 80, border_thickness: int = 40,
                font=pg.font.SysFont('Consolas', 30), screen=pg.display.set_mode((1280, 720)),
                board_color=pg.Color(255, 234, 230)):
    x = ["A", "B", "C", "D", "E", "F", "G", "H"]
    y = ["1", "2", "3", "4", "5", "6", "7", "8"][::-1]
    board = square_size * 8
    pg.draw.rect(screen, board_color, (0, 0, board + (border_thickness * 2),
                                       board + (border_thickness * 2)), border_thickness)
    for i in range(8):
        text = font.render(x[i], False, (0, 0, 0))
        screen.blit(text, (border_thickness + (i * square_size) + (square_size / 2) - 10,
                           border_thickness + (square_size * 8) + 5))
        text = font.render(y[i], False, (0, 0, 0))
        screen.blit(text, ((border_thickness / 2) - 5,
                           border_thickness + (i * square_size) + (square_size / 2) - 10))
    location = (border_thickness, border_thickness)
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = pg.Color("white")
            else:
                color = pg.Color("gray")
            pg.draw.rect(screen, color, (location[0] + col * square_size, location[1] + row * square_size,
                                         square_size, square_size))
