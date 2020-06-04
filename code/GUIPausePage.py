import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

display_width = 1024
display_height = 768

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')
clock = pygame.time.Clock()
def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, x_displace = 0,y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(x_displace / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)

def pause():
    paused = True
    bg_img = pygame.Surface((display_width, display_height))
    # bg_img.set_colorkey(black)
    bg_img.set_alpha(150)
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

        Infantry = pygame.image.load("../img/Infantry-self.png")
        Infantry = pygame.transform.scale(Infantry,(50,50))
        gameDisplay.blit(Infantry,(50,50))
        message_to_screen("Infantry",white,360,-310,size="small")
        message_to_screen("> Move : 3 pix",white,250,-250)
        message_to_screen("> ATK : 1 pix  ",white,250,-200)
        # message_to_screen("> Total ATK : No limit",white,335,-150)

        Mech = pygame.image.load("../img/Mech-self.png")
        Mech = pygame.transform.scale(Mech,(50,50))
        gameDisplay.blit(Mech,(50,250))
        message_to_screen("Mech",white,360,-110)
        message_to_screen("> Move : 2 pix",white,250,-50)
        message_to_screen("> ATK : 1 pix  ",white,250,0)

        Reco = pygame.image.load("../img/Reco-self.png")
        Reco = pygame.transform.scale(Reco,(50,50))
        gameDisplay.blit(Reco,(50,450))
        message_to_screen("Reco",white,360,100)
        message_to_screen("> Move : 2 pix",white,250,160)
        message_to_screen("> ATK : 1 pix  ",white,250,210)

        APC = pygame.image.load("../img/APC-self.png")
        APC = pygame.transform.scale(APC,(50,50))
        gameDisplay.blit(APC,(50,650))

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








