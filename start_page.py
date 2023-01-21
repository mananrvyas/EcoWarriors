import pygame
import redirect_screen
# # Initialize pygame and set the window size
# pygame.init()
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# width, height = pygame.display.get_surface().get_size()
#
# # Load the background image and set it as the background
# bg = pygame.image.load("bg.png")
# screen.blit(bg, (0, 0))
#
# # Define the button images
# button1_img = pygame.image.load("button1.png")
# button2_img = pygame.image.load("button2.png")
# button3_img = pygame.image.load("button3.png")
#
# # Set the width of the button images to 80 pixels and adjust the height proportionally
# button_width = 80
# button1_img = pygame.transform.scale(button1_img, (button_width, int(button1_img.get_height() * button_width / button1_img.get_width())))
# button2_img = pygame.transform.scale(button2_img, (button_width, int(button2_img.get_height() * button_width / button2_img.get_width())))
# button3_img = pygame.transform.scale(button3_img, (button_width, int(button3_img.get_height() * button_width / button3_img.get_width())))
# # Position the buttons on the screen
# button1_rect = button1_img.get_rect(center=(width // 2, height * 2 / 5))
# button2_rect = button2_img.get_rect(center=(width // 2, height * 3 / 5))
# button3_rect = button3_img.get_rect(center=(width // 2, height * 4 / 5))
#
# # Draw the buttons on the screen
# screen.blit(button1_img, button1_rect)
# screen.blit(button2_img, button2_rect)
# screen.blit(button3_img, button3_rect)
#
# # Create a variable to keep track of the current button
# current_button = 1
#
# # Main game loop
# running = True
#
# while running:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         # Check for arrow key presses
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 if current_button > 1:
#                     current_button -= 1
#             elif event.key == pygame.K_DOWN:
#                 if current_button < 3:
#                     current_button += 1
#             elif event.key == pygame.K_SPACE:
#                 # Perform action for the selected button
#                 if current_button == 1:
#                     print("Button 1 selected")
#                 elif current_button == 2:
#                     if not redirect_screen.show_new_screen(screen, "about_page.png"):
#                         # redraw the previous screen
#                         screen.blit(bg, (0, 0))
#                         screen.blit(button1_img, button1_rect)
#                         screen.blit(button2_img, button2_rect)
#                         screen.blit(button3_img, button3_rect)
#                         pygame.display.update()
#                 elif current_button == 3:
#                     print("Button 3 selected")
#                     running = False
#     pygame.display.update()
#
# # Quit pygame
# pygame.quit()
#
#
# # Quit pygame
# pygame.quit()
#

# Initialize pygame and set the window size


# Initialize pygame and set the window size
# import pygame
# import redirect_screen

# Initialize pygame and set the window size
import pygame
import redirect_screen

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = pygame.display.get_surface().get_size()
bg = pygame.image.load("bg.png")
screen.blit(bg, (0, 0))
font_normal = pygame.font.Font(None, 40)
font_bold = pygame.font.Font(None, 80, bold=True)
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
                    print("Button 1 selected")
                elif current_button == 2:
                    if not redirect_screen.show_new_screen(screen, "about_page.png"):
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
        button1_surf = font_bold.render(button1_text, True, (255, 255, 255))
        button2_surf = font_normal.render(button2_text, True, (255, 255, 255))
        button3_surf = font_normal.render(button3_text, True, (255, 255, 255))
    elif current_button == 2:
        button1_surf = font_normal.render(button1_text, True, (255, 255, 255))
        button2_surf = font_bold.render(button2_text, True, (255, 255, 255))
        button3_surf = font_normal.render(button3_text, True, (255, 255, 255))
    elif current_button == 3:
        button1_surf = font_normal.render(button1_text, True, (255, 255, 255))
        button2_surf = font_normal.render(button2_text, True, (255, 255, 255))
        button3_surf = font_bold.render(button3_text, True, (255, 255, 255))
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
