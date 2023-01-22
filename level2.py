import pygame

def screen2():
    # Initialize the screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = pygame.display.get_surface().get_size()
    # Load the background image 
    bg = pygame.image.load("evil.png")
    screen.blit(bg, (0, 0))
    x = 280
    y = 540
    # Position the images on the screen
    # Keep track of which image is currently visible
    final_bg = pygame.image.load("evil_final.png")
    # Keep track of which image is currently visible
    sprite = pygame.image.load('leftwalk.png')  # Added the sprite (main character)
    sprite = pygame.transform.scale(sprite, (
        sprite.get_width() * 0.6, sprite.get_height()*0.6))
    screen.blit(bg, (0, 0))
    screen.blit(sprite, (x, y))
    pygame.display.update()
    pygame.time.delay(2000)
    task_count = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

        keys = pygame.key.get_pressed()
        vel = 10

        surface = pygame.display.get_surface()

        trees = pygame.image.load("final_view.png")        
        h = surface.get_height()
        y_max = h - 1
        w = surface.get_width()
        x_max = w - 1

        if keys[pygame.K_RIGHT] and x < 0.9 * x_max:
            sprite = pygame.image.load('rightwalk.png')  # Added the sprite (main character)
            sprite = pygame.transform.scale(sprite, (
                sprite.get_width() * 0.6, sprite.get_height() * 0.6))
            x += vel
        if keys[pygame.K_LEFT] and x > 1:
            sprite = pygame.image.load(
                'leftwalk.png')  # Added the sprite (main character)
            sprite = pygame.transform.scale(sprite, (
                sprite.get_width() * 0.6, sprite.get_height() * 0.6))
            x -= vel
        if keys[pygame.K_UP] and y > 0.55 * y_max:
            y -= vel
        if keys[pygame.K_DOWN] and y < 0.56 * y_max:
            y += vel
        # pygame.time.delay(1000)
        screen.blit(final_bg, (0,0))
        screen.blit(sprite, (x, y))
        for i in range(600, -400, -50):
                # print(i)
            pygame.display.update()
            npchar = pygame.image.load(
            'npc_happy.png')
            npchar = pygame.transform.scale(npchar, (
            npchar.get_width() * 0.9, npchar.get_height() * 0.9))
            x_pos = 1000
            y_pos = 320
            pygame.time.delay(400)
            screen.blit(final_bg , (0, 0))
            screen.blit(sprite, (x, y))
            screen.blit(npchar, (x_pos + i, y_pos))
            pygame.display.update()
            running = False
        screen.blit(trees, (0, 0))
        screen.blit(sprite, (x, y))
        # pygame.time.delay(2000)
        # pygame.display.update()
        # Tree background for ending



screen2()