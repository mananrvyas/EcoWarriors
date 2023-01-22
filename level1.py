import time

import pygame

def screen1():
    # Initialize the screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = pygame.display.get_surface().get_size()
    # Load the background image
    bg = pygame.image.load("Level_1.png")
    screen.blit(bg, (0, 0))
    x = 280
    y = 570
    # Load the other 6 images
    img1 = pygame.image.load("trash6.png")
    img1 = pygame.transform.scale(img1, (
        img1.get_width() * 0.5, img1.get_height() * 0.5))
    screen.blit(img1, (x, y))

    img2 = pygame.image.load("trash5.png")
    img2 = pygame.transform.scale(img2, (
        img2.get_width() * 0.5, img2.get_height() * 0.5))
    screen.blit(img2, (x, y))
    img3 = pygame.image.load("trash4.png")
    img3 = pygame.transform.scale(img3, (
        img3.get_width() * 0.5, img3.get_height() * 0.5))
    screen.blit(img3, (x, y))

    img4 = pygame.image.load("trash3.png")
    img4 = pygame.transform.scale(img4, (
        img4.get_width() * 0.5, img4.get_height() * 0.5))
    screen.blit(img4, (x, y))

    img5 = pygame.image.load("trash2.png")
    img5 = pygame.transform.scale(img5, (
        img5.get_width() * 0.5, img5.get_height() * 0.5))
    screen.blit(img1, (x, y))

    img6 = pygame.image.load("trash1.png")
    img6 = pygame.transform.scale(img6, (
        img6.get_width() * 0.5, img6.get_height() * 0.5))
    screen.blit(img6, (x, y))
    # Position the images on the screen
    img1_rect = img1.get_rect(topleft=(800, 800))
    img2_rect = img2.get_rect(topleft=(1420, 850))
    img3_rect = img3.get_rect(topleft=(950, 760))
    img4_rect = img4.get_rect(topleft=(1550, 700))
    img5_rect = img5.get_rect(topleft=(1500, 780))
    img6_rect = img6.get_rect(topleft=(600, 750))
    # Keep track of which image is currently visible
    images = [img1, img2, img3, img4, img5, img6]
    rects = [img1_rect, img2_rect, img3_rect, img4_rect, img5_rect, img6_rect]
    final_bg = pygame.image.load("Level_1_final.png")
    # Keep track of which image is currently visible
    sprite = pygame.image.load(
        'leftwalk.png')  # Added the sprite (main character)
    sprite = pygame.transform.scale(sprite, (
        sprite.get_width() * 0.5, sprite.get_height() * 0.5))
    screen.blit(sprite, (x, y))
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
            npchar = pygame.image.load(
                'npc.png')  # Added the sprite (main character)
            npchar = pygame.transform.scale(npchar, (
                npchar.get_width() * 0.8, npchar.get_height() * 0.8))
            x_pos = 1000
            y_pos = 450
            # screen.blit(npchar, (x_pos, y_pos))
            # pygame.display.update()
            # screen.blit(npchar, (x_pos, y_pos))
            # screen.blit(npchar, (x_pos, y_pos))
            # pygame.time.get_ticks()
            # aa = 22222*3456987867868
            # pygame.time.wait(4000)
            for i in range(600, -400, -50):
                # print(i)
                screen.blit(final_bg, (0, 0))
                screen.blit(sprite, (x, y))
                pygame.time.delay(400)
                screen.blit(npchar, (x_pos + i, y_pos))
                pygame.display.update()
            pygame.time.delay(7000)
            running = False


        else:
            screen.blit(bg, (0, 0))

            for i in range(6 - image_count):
                screen.blit(images[i], rects[i])

        keys = pygame.key.get_pressed()
        # print(keys)
        vel = 10

        surface = pygame.display.get_surface()
        h = surface.get_height()
        y_max = h - 1
        w = surface.get_width()
        x_max = w - 1

        if keys[pygame.K_RIGHT] and x < 0.9 * x_max:
            sprite = pygame.image.load(
                'rightwalk.png')  # Added the sprite (main character)
            sprite = pygame.transform.scale(sprite, (
                sprite.get_width() * 0.5, sprite.get_height() * 0.54))
            x += vel
        if keys[pygame.K_LEFT] and x > 1:
            sprite = pygame.image.load(
                'leftwalk.png')  # Added the sprite (main character)
            sprite = pygame.transform.scale(sprite, (
                sprite.get_width() * 0.5, sprite.get_height() * 0.54))
            x -= vel
        if keys[pygame.K_UP] and y > 0.57 * y_max:
            y -= vel
        if keys[pygame.K_DOWN] and y < 0.57 * y_max:
            y += vel

        screen.blit(sprite, (x, y))

        pygame.display.update()

    pygame.quit()