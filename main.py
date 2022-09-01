"""
from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

# printing enum member as string
print(Season.SPRING)

# printing name of enum member using "name" keyword
print(Season.SPRING.name)

# printing value of enum member using "value" keyword
print(Season.SPRING.value)

# printing the type of enum member using type()
print(type(Season.SPRING))

# printing enum member as repr
print(repr(Season.SPRING))

# printing all enum member using "list" keyword
print(list(Season))"""

# Comment
import pygame
import sys

ui = True

if ui:
    pygame.init()

    size = width, height = 1320, 1240
    square_size = 40
    speed = [1, 1]
    black = 0, 0, 0
    white = 255, 255, 255

    gameDisplay = pygame.display.set_mode(size)
    boardLength = 8
    gameDisplay.fill(white)

    piece = pygame.image.load("piece.png")
    board = pygame.image.load("Chess_Board.jpg")
    pygame.display.set_caption('Quick Start')

    piece_rect = piece.get_rect()
    board_rect = board.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        piece_rect = piece_rect.move(speed)
        if piece_rect.left < 0 or piece_rect.right > width:
            speed[0] = -speed[0]
        if piece_rect.top < 0 or piece_rect.bottom > height:
            speed[1] = -speed[1]

        gameDisplay.fill(black)
        gameDisplay.blit(piece, piece_rect)
        gameDisplay.blit(board, board_rect)
        pygame.display.flip()


#
#
# for event in pygame.event.get():
#     if event.type == pygame.QUIT: sys.exit()
#
# # set color with rgb
# white, black, red = (255, 255, 255), (0, 0, 0), (255, 0, 0)
#
# # set display
# gameDisplay = pygame.display.set_mode((1920, 980))
#
# # Size of squares
# size = 20
#
# # Board length, must be even
# boardLength = 8
# gameDisplay.fill(white)
#
# cnt = 0
# for i in range(1, boardLength + 1):
#     for z in range(1, boardLength + 1):
#         # check if current loop value is even
#         if cnt % 2 == 0:
#             pygame.draw.rect(gameDisplay, white, [size * z, size * i, size, size])
#         else:
#             pygame.draw.rect(gameDisplay, black, [size * z, size * i, size, size])
#         cnt += 1
#     # since theres an even number of squares go back one value
#     cnt -= 1
# # Add a nice boarder
# pygame.draw.rect(gameDisplay, black, [size, size, boardLength * size, boardLength * size], 1)
#
# pygame.display.update()


class Chess:
    class Piece():

        def __init__(self, type_of_piece, coordinates):  # constructor
            print(coordinates)
            self.ptype = type_of_piece
            self.y, self.x = coordinates
            print("class starts here")

    class Pawn:
        def moveset(self, y, x, fx, fy, chess_board):
            print(chess_board[fy][fx])
            chess_board[fy][fx] = chess_board[x][y]

            print(chess_board[fy][fx])
            chess_board[y][x] = [0, 0]
            print("\n")
            if chess_board[y][x][1] != 0 and chess_board[y][x][1] != chess_board[fy][fx][1]:
                print("ENEMY ATTACKED")
            for a in range(len(chess_board)):
                print(chess_board[a])
            return chess_board

    class Knight:
        def moveset(self, y, x, fx, fy, chess_board):
            print(chess_board[fy][fx])
            chess_board[fy][fx] = chess_board[x][y]

            print(chess_board[fy][fx])
            chess_board[y][x] = [0, 0]
            print("\n")
            if chess_board[y][x][1] != 0 and chess_board[y][x][1] != chess_board[fy][fx][1]:
                print("ENEMY ATTACKED")
            for a in range(len(chess_board)):
                print(chess_board[a])
            return chess_board

    class King:
        def moveset(self, y, x, fx, fy, chess_board):
            print(chess_board[fy][fx])
            chess_board[fy][fx] = chess_board[x][y]

            print(chess_board[fy][fx])
            chess_board[y][x] = [0, 0]
            print("\n")
            if chess_board[y][x][1] != 0 and chess_board[y][x][1] != chess_board[fy][fx][1]:
                print("ENEMY ATTACKED")
            for a in range(len(chess_board)):
                print(chess_board[a])
            return chess_board

    class Queen:
        def moveset(self, y, x, fx, fy, chess_board):
            print(chess_board[fy][fx])
            chess_board[fy][fx] = chess_board[x][y]

            print(chess_board[fy][fx])
            chess_board[y][x] = [0, 0]
            print("\n")
            if chess_board[y][x][1] != 0 and chess_board[y][x][1] != chess_board[fy][fx][1]:
                print("ENEMY ATTACKED")
            for a in range(len(chess_board)):
                print(chess_board[a])
            return chess_board

    class Bishop:
        def moveset(self, y, x, fx, fy, chess_board):
            print(chess_board[fy][fx])
            chess_board[fy][fx] = chess_board[x][y]

            print(chess_board[fy][fx])
            chess_board[y][x] = [0, 0]
            print("\n")
            if chess_board[y][x][1] != 0 and chess_board[y][x][1] != chess_board[fy][fx][1]:
                print("ENEMY ATTACKED")
            for a in range(len(chess_board)):
                print(chess_board[a])
            return chess_board

    class Rook:
        def moveset(self, y, x, fx, fy, chess_board):
            print(chess_board[fy][fx])
            chess_board[fy][fx] = chess_board[x][y]

            print(chess_board[fy][fx])
            chess_board[y][x] = [0, 0]
            print("\n")
            if chess_board[y][x][1] != 0 and chess_board[y][x][1] != chess_board[fy][fx][1]:
                print("ENEMY ATTACKED")
            for a in range(len(chess_board)):
                print(chess_board[a])
            return chess_board

    chess_board2 = [
        [[5, 2], [4, 2], [3, 2], [1, 2], [6, 2], [3, 2], [4, 2], [5, 2]],  # y0
        [[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2]],  # y1
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # y2
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # y3
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # y4
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # y5
        [[2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1]],  # y6
        [[5, 1], [4, 1], [3, 1], [6, 1], [1, 1], [3, 1], [4, 1], [5, 1]]]  # y7
    #     x0       x1       x2     x3      x4       x5      x6      x7

    chess_board2 = Pawn.moveset(0, 1, 1, 5, 0, chess_board2)
    for x in range(len(chess_board2)):
        print(chess_board2[x])
    # pawn = Piece("Pawn")
    # knight = Piece("Knight")
    # king = Piece("king")
    # queen = Piece("queen")
    # bishop = Piece("bishop")

    piece_coordinates = chess_board2[0][0]
    rook = Piece("rook", piece_coordinates)
    print(rook.x)
    print(rook.y)
    print(rook.ptype)

    """
    chess_board[y] [x] [data]
    """
    """
    type_of_piece, Enemy/Ally)
    The King == 1
    The Pawn == 2
    The Bishop == 3
    The Knight == 4
    The Rook == 5
    The Queen == 6

    (0 , 0) == empty
    (x , 1) == white
    (x , 2) == black
    """

    for x in range(len(chess_board2)):
        print(chess_board2[x])
    turn = 1
    while True:

        if turn % 2 == 1:
            print("White's turn")
        else:
            print("Black's turn")
        turn += turn

        print("Current position: ")
        print(f"x = ")
        x = input()  # x == string
        x = int(x)  # now x == int   (we need to find better way to do that)
        print(f"y = ")
        y = input()
        y = int(y)

        print("Future position: ")
        print(f"x = ")
        fx = input()
        fx = int(fx)
        print(f"y = ")
        fy = input()
        fy = int(fy)

        if chess_board2[y][x][0] == 0:
            print("EMPTY")
            print("King")
            chess_board2 = King.moveset(0, y, x, fy, fx, chess_board2)
        if chess_board2[y][x][0] == 2:
            print("Pawn")
            chess_board2 = King.moveset(0, y, x, fy, fx, chess_board2)
        if chess_board2[y][x][0] == 3:
            print("Bishop")
            chess_board2 = King.moveset(0, y, x, fy, fx, chess_board2)
        if chess_board2[y][x][0] == 4:
            print("Knight")
            chess_board2 = King.moveset(0, y, x, fy, fx, chess_board2)
        if chess_board2[y][x][0] == 5:
            print("Rook")
            chess_board2 = King.moveset(0, y, x, fy, fx, chess_board2)
        if chess_board2[y][x][0] == 6:
            print("Queen")
            chess_board2 = King.moveset(0, y, x, fy, fx, chess_board2)

        # if clicked button == ` then break:
