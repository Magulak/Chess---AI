import pygame
from PIL import Image


def draw_chessboard(surface):
    for i in range(0, 8):
        for j in range(0, 8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(surface, black, (i * 87, j * 87, 87, 87))


# Window size
window_size = (700, 700)

pygame.init()
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption("Chess Board")

# Load and resize image
image = Image.open("Piece.png")
image = image.resize((87, 87))
image.save("Piece1.png")

# Load resized image
image = pygame.image.load('Piece1.png').convert()

# Make image see-through
image.set_alpha(200)

# list of pieces and their position
piece_position_list = []

piece_dragging = False

# TODO WHITE PIECES
# Create rect based on image, and set its basic coordinates. and make 7 copies of that piece, and set them on board
# PAWN
piece = image.get_rect()
piece.x, piece.y = 0, 87
x = 1
while x <= 8:
    exec(f"piece{x} = piece.copy()\n"
         f"piece_position_list.append(piece{x})\n"
         f"piece.x, piece.y = x*87,87")
    x = x + 1
    # KNIGHT
    # BISHOP
    # ROOK
    # QUEEN
    # KING

# TODO BLACK PIECES
# PAWN
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

clock = pygame.time.Clock()

# Create back buffer and fill it with white color.
# Back_buffer will keep chess board in memory, so chess board won't be generated every iteration.
back_buffer = pygame.Surface((screen.get_width(), screen.get_height()))
back_buffer.fill(white)

# TODO make so pieces 'lock in' the centre of a square.
# TODO add more pieces.
while running:

    # --------------------------------------------  EVENTS  --------------------------------------------
    # Stop running if pygame window closed.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect left mouse click-hold.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for piece in piece_position_list:  # Consider collision for every coordinate in list.
                    if piece.collidepoint(event.pos):
                        piece_dragging = True
                        dragged_piece = piece
                        mouse_x, mouse_y = event.pos
                        offset_x = piece.x - mouse_x  # Offset - distance between right upper corner of image and cursor
                        offset_y = piece.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                piece_dragging = False
                dragged_piece = None  # Dragged piece needs to be specified, otherwise all pieces react to dragging.

        # Overwrite piece's current position with cursors position + offset
        elif event.type == pygame.MOUSEMOTION:
            if piece_dragging:
                for piece in piece_position_list:
                    mouse_x, mouse_y = event.pos
                    dragged_piece.x = mouse_x + offset_x
                    dragged_piece.y = mouse_y + offset_y

    # ---------------------------------------  END OF EVENTS ------------------------------------------------------

    # Fill the screen with white
    screen.fill(white)

    # Draw the chess board
    draw_chessboard(back_buffer)
    screen.blit(back_buffer, (0, 0))

    # Draw images of chess pieces on chess board
    for piece in piece_position_list:
        screen.blit(image, piece)

    # Update the display
    pygame.display.flip()

# Exit Pygame
pygame.quit()
