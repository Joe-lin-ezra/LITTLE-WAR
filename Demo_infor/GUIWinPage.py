import pygame
import time
import GUINewGamePageButtonClick
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
yellow = (255, 255, 000)

smallfont = pygame.font.SysFont("Agency FB", 25)
medfont = pygame.font.SysFont("Agency FB", 50)
largefont = pygame.font.SysFont("Agency FB", 140)

display_width = 1024
display_height = 768

clock = pygame.time.Clock()

RankBtn = pygame.image.load("../img/RankBtn.png")
RankBtn2 = pygame.image.load("../img/RankBtn2.png")

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





# WinPage()








