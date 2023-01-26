import pygame
from PIL import Image

# chessboard size
size = (700, 700)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess Board")

# Load and resize image
image = Image.open("Piece.png")
image = image.resize((87, 87))
image.save("Piece1.png")

# Load resized image and create rect based on that image
image = pygame.image.load('Piece1.png').convert()
piece = image.get_rect()

# list of pieces and their position
collide_list = []

piece_draging = False

x = 0
while x <= 7:
    exec(f"piece{x} = piece.copy()\ncollide_list.append(piece{x})")
    x = x + 1
for i, value in enumerate(collide_list):
    print(f"Index: {i}, Value: {value}")


# Define the colors & fps
white = (255, 255, 255)
black = (0, 0, 0)
fps = 30

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for piece in collide_list:  # Multiple object collision
                    if piece.collidepoint(event.pos):
                        piece_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = piece.x - mouse_x
                        offset_y = piece.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                piece_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if piece_draging:
                mouse_x, mouse_y = event.pos
                piece.x = mouse_x + offset_x
                piece.y = mouse_y + offset_y

    # Fill the screen with white
    screen.fill(white)
    pygame.draw.rect(screen, white, piece)
    pygame.display.flip()  # TODO screen blinks cause you redraw it all the time, create back buffer
    # TODO set image as background, cause its wasting cpu power.
    # Draw the chess board
    for i in range(0, 8):
        for j in range(0, 8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, black, (i * 87, j * 87, 87, 87))


    # screen.blit(image, piece)
    screen.blit(image, collide_list[0])
    screen.blit(image, collide_list[1])
    screen.blit(image, collide_list[2])
    screen.blit(image, collide_list[3])
    screen.blit(image, collide_list[4])  # TODO FIX THIS !!!
    screen.blit(image, collide_list[5])
    screen.blit(image, collide_list[6])
    screen.blit(image, collide_list[7])
    # Update the display
    pygame.display.flip()

# Exit Pygame
pygame.quit()
