def board_state():
    return [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]


def insert_piece(board_, piece):
    board_[piece.location[0]][piece.location[1]] = piece
    return board_


def remove_piece(board_, piece):
    board_[piece.location[0]][piece.location[1]] = 0


def move_piece(board_, from_location, to_location):
    board_[to_location[0]][to_location[1]] = board_[from_location[0]][from_location[1]]
    board_[to_location[0]][to_location[1]].location = to_location
    print(board_[to_location[0]][to_location[1]].location)
    board_[from_location[0]][from_location[1]] = 0
    return board_
