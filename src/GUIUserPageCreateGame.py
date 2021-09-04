import pygame
import GUINewGamePageTextBox


display_width = 1024
display_height = 768

gameDisplay = pygame.display.set_mode((1024, 768))

pygame.display.set_caption('Tanks')

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 000)

blue = (51, 102, 255)
light_blue = (102, 153, 255)

red = (200, 0, 0)
light_red = (255, 0, 0)

green = (0, 153, 51)
light_green = (51, 204, 51)

brown = (153, 102, 51)

gray = (102, 102, 102)
light_gray = (230, 230, 230)

clock = pygame.time.Clock()

# 字型的東西 By Chin - Head#
pygame.font.init()
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, x_displace=0, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(x_displace / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)



def game_CreateGame(num):
    pygame.init()
    intro = True

    textinputName = GUINewGamePageTextBox.TextInput()           # TextBox for UserName
    textinputPw = GUINewGamePageTextBox.TextInput()             # TextBox for Set up Password
    textinputPwC = GUINewGamePageTextBox.TextInput()            # TextBox for Confirm Password
    TextArea = pygame.Surface((400, 55))
    TextArea.fill(light_gray)
    token = 0
    while intro:
        gameDisplay.fill(yellow)

        events = pygame.event.get()
        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        message_to_screen("UserName", black, 1000, -130, size='medium')
        gameDisplay.blit(TextArea, (300, 350))
        gameDisplay.blit(textinputName.get_surface(), (310, 360))
        if textinputName.update(events):
            Name = textinputName.get_text()         # 在此取得UserName
            net.send({'event': 6, 'name': Name, 'num': num})
            print(Name)
        pygame.display.update()
        clock.tick(30)



# game_CreateGame()
