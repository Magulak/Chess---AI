import pygame
from PIL import Image


def draw_chessboard(surface):
    for i in range(0, 8):
        for j in range(0, 8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(surface, black, (i * 87, j * 87, 87, 87))


# Window size
size = (700, 700)

pygame.init()
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Chess Board")

# Load and resize image
image = Image.open("Piece.png")
image = image.resize((87, 87))
image.save("Piece1.png")

# Load resized image
image = pygame.image.load('Piece1.png').convert()



# list of pieces and their position
piece_position_list = []

piece_draging = False


# Create rect based on image, and set its basic coordinates. and make 7 copies of that piece, and set them on board
piece = image.get_rect()
piece.x, piece.y = 0, 87
x = 1
while x <= 8:
    exec(f"piece{x} = piece.copy()\n"
         f"piece_position_list.append(piece{x})\n"
         f"piece.x, piece.y = x*87,87")
    x = x + 1

# Define the colors & fps
white = (255, 255, 255)
black = (0, 0, 0)
fps = 30
running = True

clock = pygame.time.Clock()

# create back buffer and fill it with white color
back_buffer = pygame.Surface((screen.get_width(), screen.get_height()))
back_buffer.fill(white)
# TODO make so pieces 'lock in' the centre of a square.
# TODO add more pieces.
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for piece in piece_position_list:  # Multiple object collision
                    if piece.collidepoint(event.pos):
                        piece_draging = True
                        draged_piece = piece
                        mouse_x, mouse_y = event.pos
                        offset_x = piece.x - mouse_x
                        offset_y = piece.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                piece_draging = False
                draged_piece = None

        elif event.type == pygame.MOUSEMOTION:
            if piece_draging:
                for piece in piece_position_list:
                    mouse_x, mouse_y = event.pos
                    draged_piece.x = mouse_x + offset_x
                    draged_piece.y = mouse_y + offset_y

    # Fill the screen with white
    screen.fill(white)

    # Draw the chess board
    draw_chessboard(back_buffer)

    screen.blit(back_buffer, (0, 0))

    for piece in piece_position_list:
        screen.blit(image, piece)

    # Update the display
    pygame.display.flip()

# Exit Pygame
pygame.quit()
