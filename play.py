import pygame

def screen1():
    # Initialize the screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = pygame.display.get_surface().get_size()
    # Load the background image
    bg = pygame.image.load("Level_1.png")
    screen.blit(bg, (0, 0))
    # Load the other 6 images
    img1 = pygame.image.load("trash6.png")
    img2 = pygame.image.load("trash5.png")
    img3 = pygame.image.load("trash4.png")
    img4 = pygame.image.load("trash3.png")
    img5 = pygame.image.load("trash2.png")
    img6 = pygame.image.load("trash1.png")
    # Position the images on the screen
    img1_rect = img1.get_rect(topleft=(10, 10))
    img2_rect = img2.get_rect(topleft=(50, 50))
    img3_rect = img3.get_rect(topleft=(100, 100))
    img4_rect = img4.get_rect(topleft=(150, 150))
    img5_rect = img5.get_rect(topleft=(200, 200))
    img6_rect = img6.get_rect(topleft=(250, 250))
    # Keep track of which image is currently visible
    images = [img1, img2, img3, img4, img5, img6]
    rects = [img1_rect, img2_rect, img3_rect, img4_rect, img5_rect, img6_rect]
    final_bg = pygame.image.load("Level_1_final.png")
    # Keep track of which image is currently visible
    image_count = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    image_count += 1
                    if image_count > 6:
                        image_count = 6
        if image_count == 6:
            screen.blit(final_bg, (0, 0))
        else:
            screen.blit(bg, (0, 0))
            for i in range(6 - image_count):
                screen.blit(images[i], rects[i])
        pygame.display.update()
    pygame.quit()


