import time

import pygame

def screen0():
    # Initialize the screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = pygame.display.get_surface().get_size()
    # Load the background image
    bg = pygame.image.load("lvwateron.png")
    screen.blit(bg, (0, 0))
    x = 280
    y = 540
    # Position the images on the screen
    # Keep track of which image is currently visible
    final_bg = pygame.image.load("lvwateroff.png")
    # Keep track of which image is currently visible
    sprite = pygame.image.load('leftwalk.png')  # Added the sprite (main character)
    sprite = pygame.transform.scale(sprite, (
        sprite.get_width(), sprite.get_height()))
    screen.blit(sprite, (x, y))
    task_count = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    screen.blit(final_bg, (0, 0))
                    sprite = pygame.image.load('leftwalk.png')  # Added the sprite (main character)
                    sprite = pygame.transform.scale(sprite, (
                    sprite.get_width(), sprite.get_height()))
                    screen.blit(sprite, (x, y))

                    pygame.display.update()
                    pygame.time.delay(10000)
                    running = False
        screen.blit(bg, (0, 0))

        keys = pygame.key.get_pressed()
        vel = 10

        surface = pygame.display.get_surface()

        h = surface.get_height()
        y_max = h - 1
        w = surface.get_width()
        x_max = w - 1

        if keys[pygame.K_RIGHT] and x < 0.9 * x_max:
            sprite = pygame.image.load('rightwalk.png')  # Added the sprite (main character)
            sprite = pygame.transform.scale(sprite, (
                sprite.get_width(), sprite.get_height()))
            x += vel
        if keys[pygame.K_LEFT] and x > 1:
            sprite = pygame.image.load(
                'leftwalk.png')  # Added the sprite (main character)
            sprite = pygame.transform.scale(sprite, (
                sprite.get_width(), sprite.get_height()))
            x -= vel
        if keys[pygame.K_UP] and y > 0.57 * y_max:
            y -= vel
        if keys[pygame.K_DOWN] and y < 0.57 * y_max:
            y += vel

        screen.blit(sprite, (x, y))

        pygame.display.update()

    pygame.quit()

screen0()