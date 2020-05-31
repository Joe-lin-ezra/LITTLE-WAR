import pygame

import GUINewGamePageMap
import GUINewGamePageTextBox
import GUINewGamePageButtonClick

# 負責人 Chin #
display_width = 1024
display_height = 768

gameDisplay = pygame.display.set_mode((1024, 768))

# pygame.display.set_caption('Tanks')

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



def game_newgame(gameDisplay):
    pygame.init()

    intro = True

    # 都是 TextBox 的東西 By Chin - Head#
    n = 0
    y = 0
    x = 0
    count = 0

    textinput = GUINewGamePageTextBox.TextInput()           # 建立一個Textinput 的地方
    ResponseArea = pygame.Surface((600,150))
    ResponseArea.fill(black)
    # 都是 TextBox 的東西 By Chin - Foot#

    # 呢邊是 Button 的東西 By Chin - Head #
    SendBtn = GUINewGamePageButtonClick.button(blue,750,590,170,120,"GO")  # color , x, y, width, height , text
    token = True        # 模仿回合的結束 用來不給玩家在不是自己的回合中輸入
    # 呢邊是 Button 的東西 By Chin - Foot #
    while intro:
        gameDisplay.fill(yellow)
        message_to_screen("Game Start", black, 1000, -340, size='large')
        gameDisplay.blit(ResponseArea, (80, 580))
        SendBtn.draw(gameDisplay)
        events = pygame.event.get()
        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SendBtn.isOver(pos):
                   print("Button Click!")
                   token = False                # 還未做出下一回合, 回恢權限 By Chin
            if event.type == pygame.MOUSEMOTION:
                if SendBtn.isOver(pos):
                    SendBtn.color = (light_blue)
                else :
                    SendBtn.color = (blue)


        if count < 4 and token:
            if textinput.update(events):              # 輸入指令的地方 By Chin
                # if count >= 3:
                    # 會否考慮顥示訊息 讓玩家知道不能輸入? By Chin
                ResponseArea.blit(textinput.get_surface(), (10, 30 + (y * n)))
                n += 1
                y = 30
                print(textinput.get_text())  # 透過get_text() 取得輸入的資訊 By Chin
                count += 1

        gameDisplay.blit(textinput.get_surface(), (90, 585))         # TextInput position By Chin
        GUINewGamePageMap.Map(gameDisplay)

        pygame.display.update()
        clock.tick(30)

game_newgame(gameDisplay)