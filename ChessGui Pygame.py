import pygame

size = (700, 700)
rectangle_draging = False

pygame.init()

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Chess Board")

# Load image
image = pygame.image.load('Piece.png').convert()
rect = image.get_rect()
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
                if rect.collidepoint(event.pos):
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rect.x - mouse_x
                    offset_y = rect.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rectangle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                rect.x = mouse_x + offset_x
                rect.y = mouse_y + offset_y

    # Fill the screen with white
    screen.fill(white)
    pygame.draw.rect(screen, white, rect)
    pygame.display.flip()

    # Draw the chess board
    for i in range(0, 8):
        for j in range(0, 8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, black, (i * 87, j * 87, 87, 87))
    screen.blit(image, rect)

    # Update the display
    pygame.display.flip()


# Exit Pygame
pygame.quit()
