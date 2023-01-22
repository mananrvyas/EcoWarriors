import pygame
import redirect_screen
import play

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = pygame.display.get_surface().get_size()
bg = pygame.image.load("./assets/bg.png")
screen.blit(bg, (0, 0))
font_normal = pygame.font.Font("./assets/Bungee-Regular.ttf", 40)
font_bold = pygame.font.Font("./assets/Bungee-Regular.ttf", 45)
button1_text = "play"
button2_text = "about"
button3_text = "quit"
button1_surf = font_normal.render(button1_text, True, (255, 255, 255))
button2_surf = font_normal.render(button2_text, True, (255, 255, 255))
button3_surf = font_normal.render(button3_text, True, (255, 255, 255))
button1_rect = button1_surf.get_rect(center=(width // 2, height * 2 / 5))
button2_rect = button2_surf.get_rect(center=(width // 2, height * 3 / 5))
button3_rect = button3_surf.get_rect(center=(width // 2, height * 4 / 5))
screen.blit(button1_surf, button1_rect)
screen.blit(button2_surf, button2_rect)
screen.blit(button3_surf, button3_rect)
pygame.display.update()
current_button = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if current_button > 1:
                    current_button -= 1
            elif event.key == pygame.K_DOWN:
                if current_button < 3:
                    current_button += 1
            elif event.key == pygame.K_SPACE:
                if current_button == 1:
                    # print("Button 1 selected")
                    play.screen0()
                elif current_button == 2:
                    if not redirect_screen.show_new_screen(screen,
                                                           "./assets/about_page.png"):
                        screen.blit(bg, (0, 0))
                        screen.blit(button1_surf, button1_rect)
                        screen.blit(button2_surf, button2_rect)
                        screen.blit(button3_surf, button3_rect)
                        pygame.display.update()
                elif current_button == 3:
                    print("Button 3 selected")
                    running = False
    screen.blit(bg, (0, 0))
    if current_button == 1:
        button1_surf = font_bold.render(button1_text, True, (119, 136, 153))
        button2_surf = font_normal.render(button2_text, True, (255, 255, 255))
        button3_surf = font_normal.render(button3_text, True, (255, 255, 255))
    elif current_button == 2:
        button1_surf = font_normal.render(button1_text, True, (255, 255, 255))
        button2_surf = font_bold.render(button2_text, True, (119, 136, 153))
        button3_surf = font_normal.render(button3_text, True, (255, 255, 255))
    elif current_button == 3:
        button1_surf = font_normal.render(button1_text, True, (255, 255, 255))
        button2_surf = font_normal.render(button2_text, True, (255, 255, 255))
        button3_surf = font_bold.render(button3_text, True, (119, 136, 153))
    if current_button == 1:
        screen.blit(button1_surf, button1_rect)
        screen.blit(button2_surf, button2_rect)
        screen.blit(button3_surf, button3_rect)
    elif current_button == 2:
        screen.blit(button1_surf, button1_rect)
        screen.blit(button3_surf, button3_rect)
        screen.blit(button2_surf, button2_rect)
    elif current_button == 3:
        screen.blit(button2_surf, button2_rect)
        screen.blit(button1_surf, button1_rect)
        screen.blit(button3_surf, button3_rect)
    pygame.display.update()
    #
    # screen.blit(button1_surf, button1_rect)
    # screen.blit(button2_surf, button2_rect)
    # screen.blit(button3_surf, button3_rect)
    # pygame.display.update()
pygame.quit()
