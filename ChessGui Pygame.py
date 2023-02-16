import pygame
from PIL import Image
from main import Chess

def draw_chessboard(surface):
    for i in range(0, 8):
        for j in range(0, 8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(surface, black, (i * 87, j * 87, 87, 87))
class NamedRect:
    def __init__(self, rect, var_name):
        self.rect = rect
        self.var_name = var_name

chess_board = Chess().chess_board2
# print(chess_board[0][0])  # rook [5, 2]

# Read all values from chessboard
for i in range(len(chess_board)):
    for j in range(len(chess_board[i])):
        print(f"The value at index [{i}][{j}] is {chess_board[i][j]}")
        # Using i(y) and j(x) draw that on THIS place on board

"""
 1. correlate x,y values with correct position on board
 chess_board [[?Y],[X]] returns ( piece_type, piece_color )
 
 Iterate through every chess_board value except the ones where color = 0
 for row in chess_board2:
    for piece in row:
 
"""

# TODO Read all values from chessboard , and depending on value draw that piece on board (eg. add it to
# TODO piece_position_list = []
# Window size
window_size = (700, 700)

pygame.init()
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption("Chess Board")

# Load and resize image
image = Image.open("Piece.png")
image = image.resize((87, 87))
image.save("Piece1.png")
image = pygame.image.load('Piece1.png').convert()

w_pawn_img = Image.open("w_pawn.png")
w_pawn_img = w_pawn_img.resize((87, 87))
w_pawn_img.save("w_pawn1.png")
w_pawn_img = pygame.image.load('w_pawn1.png').convert()


# Make image see-through
# image_list = [image, w_pawn_img]
image.set_alpha(200)  # every object from list of images gets chanel alpha at 200
w_pawn_img.set_alpha(200)
# for img in image_list:
#     img.set_alpha(230)

# list of pieces and their position
piece_position_list = []

piece_dragging = False
# ---------------------------------------- CREATING PIECES -----------------------------------------
# TODO BLACK PIECES
# Create rect based on image, and set its basic coordinates. and make 7 copies of that piece, and set them on board
# PAWN
b_pawn = image.get_rect()  # image.get rect method only decides size of rect based on image size
b_pawn.x, b_pawn.y = 0, 87
x = 0
while x <= 8:
    exec(f"b_pawn{x} = b_pawn.copy()\n"
         f"piece_position_list.append(NamedRect(b_pawn{x},'b_pawn'))\n"
         f"b_pawn{x}.x, b_pawn{x}.y = x*87,87") # i added {x} to b_pawn
    x = x + 1
    # KNIGHT
    # BISHOP
    # ROOK
    # QUEEN
    # KING

# TODO WHITE PIECES
# PAWN
white_pawn = w_pawn_img.get_rect()
x = 0
while x <= 8:
    exec(f"w_pawn{x} = white_pawn.copy()\n"
         f"piece_position_list.append(NamedRect(w_pawn{x},'w_pawn'))\n"
         f"w_pawn{x}.x, w_pawn{x}.y = x*87,522")
    x = x + 1
# KNIGHT
# BISHOP
# ROOK
# QUEEN
# KING


# Define the colors & fps
white = (255, 255, 255)
black = (0, 0, 0)
fps = 30
running = True

# TODO ADD COMMUNICATION NOW !!!! To forsee future problems.

clock = pygame.time.Clock()

# Create back buffer and fill it with white color.
# Back_buffer will keep chess board in memory, so chess board won't be generated every iteration.
back_buffer = pygame.Surface((screen.get_width(), screen.get_height()))
back_buffer.fill(white)


#
# def convert_to_chess_coordinates(x, y):
#     x_coordinate = chr(x // 87 + 97)
#     y_coordinate = 8 - y // 87
#     return x_coordinate + str(y_coordinate)
#
# # Example usage:
# x = 4 * 87
# y = 3 * 87
# print(convert_to_chess_coordinates(x, y)) # Output: "d6"


while running:

    # -----------------------------------------  EVENTS  --------------------------------------------
    # Stop running if pygame window closed.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect left mouse click-hold.
        elif event.type == pygame.MOUSEBUTTONDOWN: # todo make a list of lists? conentents of that lists are:
            if event.button == 1:   # todo [w_pawn_list, b_pawn_list, w_king_list] and those lists have piece's coords.
                for piece in piece_position_list:  # Consider collision for every coordinate in list.
                    if piece.rect.collidepoint(event.pos):
                        piece_dragging = True
                        dragged_piece = piece.rect
                        mouse_x, mouse_y = event.pos
                        offset_x = piece.rect.x - mouse_x  # Offset - distance between right upper corner of image and cursor
                        offset_y = piece.rect.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for piece in piece_position_list:  # this is fix for app crashing when no piece is clicked
                    if piece.rect.collidepoint(event.pos):  # Do this, if there is a piece under cursor.
                        piece_dragging = False
                        # if cursor in is in zone of a black/white square then snap it to center of that square.
                        # TODO Position of chess piece is determined by it's left upper corner, it needs better algorithm
                        # TODO Something like dragged_piece.x + 87 = (i * 87 would maybe fix it, but it's impossible to execute.
                        # TODO Crashes when clicked on nothing.
                        for i in range(0, 8):
                            for j in range(0, 8):
                                x_range = range(i * 87, (i * 87) + 87)
                                y_range = range(j * 87, (j * 87) + 87)
                                if dragged_piece.x in x_range and dragged_piece.y in y_range:
                                    # TODO SEND THIS MOVE HERE TO ENGINE TOO !!! IF IT SAYS THAT MOVE IS LEGAL THEN CONT
                                    dragged_piece.x = (i * 87)
                                    dragged_piece.y = (j * 87)


                dragged_piece = None  # Dragged piece needs to be specified, otherwise all pieces react to dragging.

        # Overwrite piece's current position with cursors position + offset
        elif event.type == pygame.MOUSEMOTION:
            if piece_dragging:
                for piece in piece_position_list:
                    mouse_x, mouse_y = event.pos
                    dragged_piece.x = mouse_x + offset_x
                    dragged_piece.y = mouse_y + offset_y

    # ---------------------------------------  END OF EVENTS ---------------------------------------------------------

    # ---------------------------------------  COMMUNICATION WITH ENGINE --------------------------------------
    # TODO Realise where are the pieces according to chessboard fields.
    # Read values from piece_position_list = [] and locate them on chess_board
    # piece.x % 87 = Pozycja na osi x
    # piece.y % 87 = Pozycja na osi y
    # --------------------------------- END OF COMMUNICATION WITH ENGINE --------------------------------------
    # ---------------------------------------  DRAWING ON BOARD ------------------------------------------------------

    # Fill the screen with white
    screen.fill(white)

    # Draw the chess board
    draw_chessboard(back_buffer)

    # Draw images of chess pieces on chess board
    screen.blit(back_buffer, (0, 0))
    b_pawn_pieces = [piece for piece in piece_position_list if piece.var_name == "b_pawn"]
    for piece in b_pawn_pieces:
        screen.blit(image, piece)

    # for piece in piece_position_list:
    #     screen.blit(image, piece)
    w_pawn_pieces = [piece for piece in piece_position_list if piece.var_name == "w_pawn"]
    for piece in w_pawn_pieces:
        screen.blit(w_pawn_img, piece)
    # Update the display
    pygame.display.flip()

    # ---------------------------------------- END OF DRAWING ON BOARD ----------------------------------------

# Exit Pygame
pygame.quit()
