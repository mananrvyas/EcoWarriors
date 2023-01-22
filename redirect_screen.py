import pygame


def show_new_screen(screen, image):
    # Load the image
    image = pygame.image.load(image)

    # Scale the image to the size of the screen
    image = pygame.transform.scale(image,
                                   (1920,1080))
    # Draw the image on the screen
    screen.blit(image, (0, 0))
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
    return False
