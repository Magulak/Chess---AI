import pygame

size = (700, 700)
piece_draging = False

pygame.init()

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Chess Board")

# Load image
image = pygame.image.load('Piece.png').convert()
piece = image.get_rect()
collidelist = []

x = 0
while x <= 7:
    exec(f"piece{x} = piece.copy()")
    exec(f"collidelist.append(piece{x})")
    x = x + 1
for i, value in enumerate(collidelist):
    print(f"Index: {i}, Value: {value}")

# rect.center = (200, 300)

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
                for piece in collidelist:  # Multiple object collision
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
    # screen.fill(white)
    pygame.draw.rect(screen, white, piece)
    pygame.display.flip()

    # Draw the chess board
    for i in range(0, 8):
        for j in range(0, 8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, black, (i * 87, j * 87, 87, 87))


    screen.blit(image, piece)
    # Update the display
    pygame.display.flip()

# Exit Pygame
pygame.quit()
