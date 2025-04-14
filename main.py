# Pygame game template

import pygame
import sys
from config import * # Import the config module
import random as rand
import draw # Import the drawing module


def init_game ():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Use constants from config

    pygame.display.set_caption(TITLE)
    return screen


def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here
    running = True
    text = "Button?"
    clickspersec = 0
    frames = 0

    def darken(color, dark):
        return (pygame.math.clamp(color[0] * dark, 0, 255),pygame.math.clamp(color[1] * dark, 0, 255),pygame.math.clamp(color[2] * dark, 0, 255),)

    # Set different values for the variables button_x and button_y
    # These two variables will position your button on the screen
    button_length = 200
    button_width = 60 
    button_x = WINDOW_WIDTH // 2
    button_y = WINDOW_HEIGHT // 2
    button_hovertime = 0
    button = pygame.Rect(button_x,button_y,button_length,button_width)
    # Define a surface for the text on the button
    # Text will be centered horizontally and vertically on the button
    surf_rect = screen.get_rect()
    surf_rect.center = button.center
    surf_rect.size = button.size
    original_button_color = (255,50,20)


    while running:
        frames += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    button_x = rand.randint(0, WINDOW_WIDTH)
                    button_y = rand.randint(0, WINDOW_HEIGHT)
                    clickspersec += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.fill(WHITE) # Use color from config

        faux_x = button_length
        faux_y = button_width

        button_color = original_button_color

        if button.collidepoint(mouse_x, mouse_y):
            button_hovertime = pygame.math.clamp((button_hovertime + 1) * 1.1, 0, 30)
            faux_x = button_length + button_hovertime
            faux_y = button_width + button_hovertime
            button_color = (darken(button_color, 0.8))
            text = "Click!"
        else:
            button_hovertime = pygame.math.clamp((button_hovertime + 1) * 0.9, 0, 30)
            faux_x = button_length + button_hovertime
            faux_y = button_width + button_hovertime
            button_color = (darken(button_color, 0.6))
            text = "Click?"

        button.size = [faux_x, faux_y]
        button.topleft = [button_x - faux_x/2, button_y - faux_y/2]
        
        pygame.draw.rect(screen, button_color, button)
        font = pygame.font.SysFont('Comic Sans MS', round(pygame.math.clamp((40 + button_hovertime * 0.8), 40, 76)), bold=True)
        font2 = pygame.font.SysFont('Comic Sans MS', round(pygame.math.clamp((40 + button_hovertime * 0.4), 40, 76)), bold=True)
        surf2 = font2.render(text, True, darken(button_color, 0.6))
        surf = font.render(text, True, darken(original_button_color, 1.5),)

        surf_rect = surf.get_rect()
        surf_rect.center = button.center
        surf_rect2 = surf2.get_rect()
        surf_rect2.center = button.center

        
        surf3 = font.render(str(clickspersec), True, (0,0,0))

        screen.blit(surf2, surf_rect2) # surf is the text for the button, and surf_rect is the surface (area on the screen) where the button text will be drawn
        screen.blit(surf, surf_rect) # surf is the text for the button, and surf_rect is the surface (area on the screen) where the button text will be drawn
        screen.blit(surf3, pygame.rect.Rect(0,0,0,0)) # surf is the text for the button, and surf_rect is the surface (area on the screen) where the button text will be drawn


        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(FPS) # Use the clock to control the frame rate

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()