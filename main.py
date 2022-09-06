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


class Chess:
    class Piece:

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
    #
    # for x in range(len(chess_board2)):
    #     print(chess_board2[x])
    # turn = 1
    # # while True:
    # #
    # #     if turn % 2 == 1:
    # #         print("White's turn")
    # #     else:
    # #         print("Black's turn")
    # #     turn += turn
    # #
    # #     print("Current position: ")
    # #     print(f"x = ")
    # #     x = input()  # x == string
    # #     x = int(x)  # now x == int   (we need to find better way to do that)
    # #     print(f"y = ")
    # #     y = input()
    # #     y = int(y)
    # #
    # #     print("Future position: ")
    # #     print(f"x = ")
    # #     fx = input()
    # #     fx = int(fx)
    # #     print(f"y = ")
    # #     fy = input()
    # #     fy = int(fy)
    # #
    # #     if chess_board2[y][x][0] == 0:
    # #         print("EMPTY")
    # #         print("King")
    # #         chess_board2 = King.moveset(0, y, x, fy, fx, chess_board2)
    # #     if chess_board2[y][x][0] == 2:
    # #         print("Pawn")
    # #         chess_board2 = King.moveset(0, y, x, fy, fx, chess_board2)
    # #     if chess_board2[y][x][0] == 3:
    # #         print("Bishop")
    # #         chess_board2 = King.moveset(0, y, x, fy, fx, chess_board2)
    # #     if chess_board2[y][x][0] == 4:
    # #         print("Knight")
    # #         chess_board2 = King.moveset(0, y, x, fy, fx, chess_board2)
    # #     if chess_board2[y][x][0] == 5:
    # #         print("Rook")
    # #         chess_board2 = King.moveset(0, y, x, fy, fx, chess_board2)
    # #     if chess_board2[y][x][0] == 6:
    # #         print("Queen")
    # #         chess_board2 = King.moveset(0, y, x, fy, fx, chess_board2)

    # TODO if clicked button == ` then break:
    pygame.init()

    square_size = width, height = 1320, 1240
    white, black, red = (255, 255, 255), (0, 0, 0), (255, 0, 0)

    chess_board_display = pygame.display.set_mode(square_size)

    chess_board_display.fill(white)
    pygame.display.set_caption('Chess--AI')

    object_width = 20
    object_height = 20
    board = pygame.image.load("Chess_Board.jpg")
    board_rect = board.get_rect()
    crashed = False

    while not crashed:

        for event in pygame.event.get():


        pygame.display.update()
        clock.tick(60)
        chess_board_display.fill(white)

        pygame.draw.rect(chess_board_display, (20, 20, 20), (500, 200, object_width, object_height))

        # pygame.display.update()  # TODO give it correct parameters.
        chess_board_display.blit(board, board_rect)
