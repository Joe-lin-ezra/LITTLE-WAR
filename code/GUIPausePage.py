import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')
clock = pygame.time.Clock()

def pause():
    paused = True
    bg_img = pygame.Surface((800, 600))
    # bg_img.set_colorkey(black)
    bg_img.set_alpha(100)
    pygame.draw.rect(bg_img, black, bg_img.get_rect())          # rect( img , border_color , img.get_rect() , border_size )

    gameDisplay.blit(bg_img, (0, 0))

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_p and pygame.key.get_mods() & pygame.KMOD_CTRL:
                #     paused = False

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                paused = False

        # gameDisplay.fill(white)

        pygame.display.update()
        clock.tick(5)




def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_p and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    pause()


        gameDisplay.fill(green)

        # button("--- Click Here To Start ---", 0, 0, 1024, 768, yellow, yellow, action="LoadingPage")

        pygame.display.update()

        clock.tick(15)

# game_intro()








